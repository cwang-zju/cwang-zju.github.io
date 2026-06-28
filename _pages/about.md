---
permalink: /
title: "About Me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
.bio { font-size: 0.95em; line-height: 1.8; margin-bottom: 1.8rem; }
.bio a { text-decoration: none; }

.news-bar {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  padding: 10px 14px;
  background: var(--global-link-color-light, #e8f0fe);
  border-radius: 6px;
  margin-bottom: 1.8rem;
  border: 0.5px solid var(--global-link-color);
}
.news-bar .news-icon { font-size: 1.1em; flex-shrink: 0; margin-top: 2px; }
.news-bar p { font-size: 0.88em; line-height: 1.6; margin: 0; color: var(--global-link-color); }

.section-label {
  font-size: 0.72em;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--global-text-color-light);
  margin: 2rem 0 0.8rem;
  padding-bottom: 0.4rem;
  border-bottom: 0.5px solid var(--global-border-color);
}

.interest-card {
  background: var(--global-code-bg-color, #f8f9fa);
  border: 0.5px solid var(--global-border-color);
  border-radius: 10px;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 14px;
}
.interest-card .ic-icon { font-size: 1.5em; flex-shrink: 0; }
.interest-card .ic-label { font-size: 0.9em; font-weight: 600; }
.interest-card .ic-sub { font-size: 0.82em; color: var(--global-text-color-light); margin-top: 2px; }

.award-list { display: flex; flex-direction: column; }
.award-row {
  display: flex;
  gap: 12px;
  align-items: baseline;
  padding: 6px 0;
  border-bottom: 0.5px solid var(--global-border-color);
  font-size: 0.88em;
}
.award-row:last-child { border-bottom: none; }
.award-year { color: var(--global-text-color-light); flex-shrink: 0; width: 36px; font-weight: 500; }
.award-badge {
  display: inline-block;
  font-size: 0.78em;
  padding: 1px 7px;
  border-radius: 10px;
  margin-left: 6px;
  font-weight: 500;
  vertical-align: middle;
}
.ab-nsf  { background: #dbeafe; color: #1e40af; }
.ab-ieee { background: #fef3c7; color: #92400e; }
.ab-odu  { background: #dcfce7; color: #166534; }

.service-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.service-block .stitle {
  font-size: 0.8em;
  font-weight: 600;
  color: var(--global-text-color-light);
  margin-bottom: 6px;
}
.tag-list { display: flex; flex-wrap: wrap; gap: 5px; }
.tag {
  font-size: 0.78em;
  padding: 2px 8px;
  background: var(--global-code-bg-color, #f8f9fa);
  border: 0.5px solid var(--global-border-color);
  border-radius: 4px;
  color: var(--global-text-color);
}
.tag.hl {
  background: #dbeafe;
  border-color: #93c5fd;
  color: #1e40af;
}
</style>

<p class="bio">
Dr. Cong Wang is an Associate Professor at the College of Control Science and Engineering,
<a href="https://www.zju.edu.cn">Zhejiang University</a>, Hangzhou, China, where he was born and raised.
He received his Ph.D from the Department of Electrical and Computer Engineering,
<a href="https://www.stonybrook.edu">Stony Brook University</a> ('16),
advised by <a href="http://www.ece.stonybrook.edu/~yang/">Prof. Yuanyuan Yang</a>,
B.Eng in Information Engineering from the <a href="https://www.cuhk.edu.hk">Chinese University of Hong Kong</a> ('08)
and M.Sc in Electrical Engineering from <a href="https://www.columbia.edu">Columbia University</a> ('09).
From 2017–2023, he was a Tenure-Track Assistant Professor at the Cybersecurity Department of
<a href="https://www.gmu.edu">George Mason University</a>, Fairfax, VA and the Computer Science Department at
<a href="https://www.odu.edu">Old Dominion University</a>, Norfolk, VA.
His research focuses on LLM Efficiency and Security.
He is the recipient of the NSF CRII Award in 2019 and NSF CAREER Award in 2021.
</p>

<div class="news-bar">
  <span class="news-icon">📢</span>
  <p><strong>New:</strong> Two papers accepted at ECCV 2026 — Vision-TTT and AEGIS. Double at ACL 2026 selected as <strong>Oral &amp; Best Paper Candidate</strong>. Congratulations to all students!</p>
</div>

<div class="section-label">Research Interests</div>

<div class="interest-card">
  <span class="ic-icon">🧠</span>
  <div>
    <div class="ic-label">LLM Efficiency and Security</div>
    <div class="ic-sub">Speculative decoding, inference acceleration, adversarial robustness, LLM safety</div>
  </div>
</div>

<div class="section-label">Awards</div>

<div class="award-list">
  <div class="award-row"><span class="award-year">2021</span><span>NSF CAREER Award<span class="award-badge ab-nsf">NSF</span></span></div>
  <div class="award-row"><span class="award-year">2021</span><span>Distinguished Research Award, ODU<span class="award-badge ab-odu">ODU</span></span></div>
  <div class="award-row"><span class="award-year">2020</span><span>Richard Cheng Research Innovation Award, ODU<span class="award-badge ab-odu">ODU</span></span></div>
  <div class="award-row"><span class="award-year">2019</span><span>NSF CRII Award<span class="award-badge ab-nsf">NSF</span></span></div>
  <div class="award-row"><span class="award-year">2018</span><span>IEEE PerCom Mark Weiser Best Paper Award<span class="award-badge ab-ieee">IEEE</span></span></div>
</div>

<div class="section-label">Services</div>

<div class="service-cols">
  <div class="service-block">
    <div class="stitle">Chairing</div>
    <div class="tag-list">
      <span class="tag hl">ACM SenSys 24 — Finance Chair</span>
      <span class="tag hl">ICNC 23 — ECB Co-Chair</span>
    </div>
  </div>
  <div class="service-block">
    <div class="stitle">Program Committee</div>
    <div class="tag-list">
      <span class="tag">INFOCOM 20–26</span>
      <span class="tag">ICDCS 23</span>
      <span class="tag">IPDPS 20</span>
      <span class="tag">All AI Conferences</span>
    </div>
  </div>
  <div class="service-block" style="margin-top:0.8rem">
    <div class="stitle">Journal Reviewer</div>
    <div class="tag-list">
      <span class="tag">TMC</span>
      <span class="tag">TON</span>
      <span class="tag">JSAC</span>
      <span class="tag">TC</span>
      <span class="tag">TWC</span>
      <span class="tag">TOSN</span>
      <span class="tag">TIS</span>
      <span class="tag">CSUR</span>
    </div>
  </div>
  <div class="service-block" style="margin-top:0.8rem">
    <div class="stitle">NSF Panelist</div>
    <div class="tag-list">
      <span class="tag">2019</span>
      <span class="tag">2020</span>
      <span class="tag">2021</span>
      <span class="tag">2022</span>
    </div>
  </div>
</div>
