require 'csv'

ORAL_PAPERS = [
  'RFF-TTA: Physical Information-Aware',
]

# Award definitions: title substring => [icon_html, label, color_class]
AWARDS = {
  'Double: Breaking the Acceleration' => ['🏆', 'SAC Highlight Award', 'award-candidate'],
  'Towards Efficient Scheduling of Federated Mobile' => ['🏆', 'Best Paper Candidate', 'award-candidate'],
  'DeepMag: Sniffing Mobile Apps' => ['🥇', 'Mark Weiser Best Paper Award', 'award-winner'],
}

def get_award(title)
  AWARDS.each do |substr, info|
    return info if title.include?(substr)
  end
  nil
end

def generate_badge(type, url)
  return "" if url.nil? || url.empty?
  logo = case type
  when 'code'   then 'github'
  when 'slides' then 'slides'
  when 'video'  then 'youtube'
  when 'paper'  then 'arxiv'
  end
  if type == 'paper' && !url.start_with?('http')
    url = "/files/#{url}" unless url.include?('/')
  end
  "<a href=\"#{url}\" style=\"text-decoration: none; margin-left: 5px;\"><img src=\"https://img.shields.io/badge/#{type}--%20?style=social&logo=#{logo}\" alt=\"#{type} link\"></a>"
end

def format_publication(pub, kind)
  venue_year = "#{pub['venue']} #{pub['pub_date'].to_s[-2..-1]}"
  title = pub['title']

  authors = pub['authors'].split(', ').map do |author|
    author.include?('Cong Wang') ? "<strong>#{author}</strong>" : author
  end.join(', ')

  badges = []
  badges << generate_badge('code',   pub['code_url'])   if pub['code_url']   && !pub['code_url'].empty?
  badges << generate_badge('slides', pub['slides_url']) if pub['slides_url'] && !pub['slides_url'].empty?
  badges << generate_badge('video',  pub['video_url'])  if pub['video_url']  && !pub['video_url'].empty?
  badges << generate_badge('paper',  pub['paper_url'])  if pub['paper_url']  && !pub['paper_url'].empty?
  badges_str = badges.empty? ? "" : " " + badges.join(' ')

  badge_cls = kind == 'conf' ? 'conf' : 'jour'

  # Award badge
  award = get_award(title)
  award_html = ""
  if award
    icon, label, cls = award
    award_html = " <span class=\"award-badge #{cls}\">#{icon} #{label}</span>"
  end

  oral_sfx = ORAL_PAPERS.any? { |s| title.include?(s) } ? ' (Oral)' : ''

  <<~HTML
    <li>
      <div class="pub-tag"><span class="pub-badge #{badge_cls}">#{venue_year}</span></div>
      <div class="pub-body"><p>
    #{title}#{award_html}<br>
    #{authors}<br>
    <em>#{pub['full_venue']}#{oral_sfx}</em>#{badges_str}
      </p></div>
    </li>
  HTML
end

def is_old(pub)
  year = pub['pub_date'].to_i
  year < 100 ? year <= 17 : year <= 2017
end

def render_section(pubs, kind)
  new_pubs = pubs.reject { |p| is_old(p) }
  old_pubs = pubs.select { |p| is_old(p) }

  new_html = new_pubs.map { |p| format_publication(p, kind) }.join("\n")
  old_html = old_pubs.map  { |p| format_publication(p, kind) }.join("\n")

  result = "<ul class=\"pub-list\">\n#{new_html}\n</ul>\n"

  unless old_pubs.empty?
    result += <<~HTML

      <button class="fold-toggle" onclick="toggleFold(this, '#{kind}-old')">
        <span class="fold-arrow">▼</span>
        Earlier work — PhD period (2010–2017)
        <span class="fold-count">#{old_pubs.size} papers</span>
      </button>
      <div class="fold-content" id="#{kind}-old">
      <ul class="pub-list">
      #{old_html}
      </ul>
      </div>
    HTML
  end
  result
end

def process_publications
  conference_pubs = CSV.read('_pages/conference.tsv', headers: true, col_sep: "\t")
  journal_pubs    = CSV.read('_pages/journel.tsv',    headers: true, col_sep: "\t")

  conference_pubs = conference_pubs.sort_by { |p| -p['pub_date'].to_i }
  journal_pubs    = journal_pubs.sort_by    { |p| -p['pub_date'].to_i }

  conf_html = render_section(conference_pubs, 'conf')
  jour_html = render_section(journal_pubs,    'jour')

  content = File.read('_pages/publications.md')
  parts = content.split(/^<h2 class="section-title">Selected Conference Publications<\/h2>\n/)
  return puts("ERROR: section header not found") unless parts.size == 2

  header = parts[0]
  rest   = parts[1].split(/^<h2 class="section-title"[^>]*>Selected Journal Publications<\/h2>\n/)

  new_content = header +
    "<h2 class=\"section-title\">Selected Conference Publications</h2>\n\n" +
    conf_html + "\n\n" +
    "<h2 class=\"section-title\" style=\"margin-top:2.5em\">Selected Journal Publications</h2>\n\n" +
    jour_html

  File.write('_pages/publications.md', new_content)
  puts "Done. publications.md updated."
end

process_publications()
