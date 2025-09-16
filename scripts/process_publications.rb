require 'csv'

def generate_badge(type, url)
  return "" if url.nil? || url.empty?
  
  logo = case type
  when 'code'
    'github'
  when 'slides'
    'slides'
  when 'video'
    'youtube'
  when 'paper'
    'arxiv'
  end

  # 处理本地文件路径
  if type == 'paper' && !url.start_with?('http')
    url = "/files/#{url}" unless url.include?('/')
  end
  
  "<a href=\"#{url}\" style=\"text-decoration: none; margin-left: 5px;\"><img src=\"https://img.shields.io/badge/#{type}--%20?style=social&logo=#{logo}\" alt=\"#{type} link\"></a>"
end

def format_publication(pub)
  # Format venue with year
  venue_year = "[#{pub['venue']} #{pub['pub_date'].to_s[-2..-1]}]"
  
  # Format authors (make Wang, Cong bold)
  authors = pub['authors'].split(', ').map do |author|
    if author.include?('Cong Wang')
      "<strong>#{author}</strong>"
    else
      author
    end
  end.join(', ')
  
  # Generate badges for available links
  badges = []
  badges << generate_badge('code', pub['code_url']) if pub['code_url']
  badges << generate_badge('slides', pub['slides_url']) if pub['slides_url']
  badges << generate_badge('video', pub['video_url']) if pub['video_url']
  badges << generate_badge('paper', pub['paper_url']) if pub['paper_url']
  badges_str = badges.empty? ? "" : " " + badges.join(' ')
  
  # Format the publication entry
  <<~HTML
    <li>
    <p>
    <strong>#{venue_year} </strong>#{pub['title']}<br>
    #{authors}<br>
    <em>#{pub['full_venue']}</em>#{badges_str}
    </p>
    </li>

  HTML
end

def process_publications
  # Read conference publications
  conference_pubs = CSV.read('_pages/conference.tsv', headers: true, col_sep: "\t")
  journal_pubs = CSV.read('_pages/journel.tsv', headers: true, col_sep: "\t")
  
  # Sort publications by date (newest first)
  conference_pubs = conference_pubs.sort_by { |pub| -pub['pub_date'].to_i }
  journal_pubs = journal_pubs.sort_by { |pub| -pub['pub_date'].to_i }
  
  # Generate HTML content
  conference_content = conference_pubs.map { |pub| format_publication(pub) }.join("\n")
  journal_content = journal_pubs.map { |pub| format_publication(pub) }.join("\n")
  
  # Read the current publications.md
  content = File.read('_pages/publications.md')
  
  # Split content at the conference and journal sections
  parts = content.split(/^## Selected Conference Publications/)
  if parts.size == 2
    header = parts[0]
    rest = parts[1].split(/^## Selected Journal Publications/)
    
    # Reconstruct the file with new content
    new_content = header + 
                 "## Selected Conference Publications\n\n" +
                 conference_content + "\n\n" +
                 "## Selected Journal Publications\n\n" +
                 journal_content + "\n"
    
    # Write back to publications.md
    File.write('_pages/publications.md', new_content)
  end
end

# Run the script
process_publications()
