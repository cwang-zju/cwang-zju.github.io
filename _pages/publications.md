---
title: "Publications"
permalink: /publications/
author_profile: true
---

<style>
.pub-section { margin-top: 0.5em; }

.section-title {
  font-size: 1.1em;
  font-weight: 700;
  color: var(--global-text-color);
  margin: 2em 0 0.8em;
  padding-bottom: 0.4em;
  border-bottom: 2px solid var(--global-link-color);
  display: flex;
  align-items: center;
  gap: 0.4em;
}

.pub-list { list-style: none; padding: 0; margin: 0; }

.pub-list li {
  display: flex;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 0.5px solid var(--global-border-color);
}
.pub-list li:last-child { border-bottom: none; }

.pub-tag {
  flex-shrink: 0;
  width: 88px;
  padding-top: 2px;
  text-align: right;
}

.pub-badge {
  display: inline-block;
  font-size: 0.7em;
  font-weight: 600;
  padding: 2px 7px;
  border-radius: 4px;
  white-space: nowrap;
  line-height: 1.6;
}
.pub-badge.conf {
  background: #dbeafe;
  color: #1e40af;
}
.pub-badge.jour {
  background: #dcfce7;
  color: #166534;
}

.pub-body { flex: 1; min-width: 0; }

.pub-body p {
  margin: 0;
  line-height: 1.5;
  font-size: 0.92em;
}

.fold-toggle {
  display: flex;
  align-items: center;
  gap: 8px;
  width: 100%;
  margin: 1em 0 0;
  padding: 8px 14px;
  border: 1px dashed var(--global-border-color);
  border-radius: 4px;
  background: var(--global-bg-color);
  cursor: pointer;
  font-size: 0.85em;
  color: var(--global-text-color-light);
  text-align: left;
}
.fold-toggle:hover { border-color: var(--global-link-color); color: var(--global-link-color); }

.fold-count {
  margin-left: auto;
  font-size: 0.78em;
  padding: 1px 8px;
  border-radius: 10px;
  background: var(--global-border-color);
  color: var(--global-text-color);
}

.fold-arrow { transition: transform 0.2s; display: inline-block; }

.fold-content { display: none; }
.fold-content.open { display: block; }

.award-badge {
  display: inline-block;
  font-size: 0.72em;
  font-weight: 600;
  padding: 1px 8px;
  border-radius: 10px;
  vertical-align: middle;
  margin-left: 6px;
}
.award-candidate {
  background: #fef9c3;
  color: #854d0e;
  border: 1px solid #fde047;
}
.award-winner {
  background: #fef3c7;
  color: #92400e;
  border: 1px solid #f59e0b;
}
</style>

<script>
function toggleFold(btn, targetId) {
  var content = document.getElementById(targetId);
  var arrow = btn.querySelector('.fold-arrow');
  content.classList.toggle('open');
  arrow.style.transform = content.classList.contains('open') ? 'rotate(180deg)' : '';
}
</script>

<div class="pub-section">

{% if site.author.googlescholar %}
You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.
{% endif %}

<h2 class="section-title">Selected Conference Publications</h2>

<ul class="pub-list">
<li>
  <div class="pub-tag"><span class="pub-badge conf">ECCV 26</span></div>
  <div class="pub-body"><p>Don’t Teach Instability, Teach Robustness: Selective Sensitivity Gating for Adversarial Robust Distillation<br>
Jingqi Ji, Quan Kong, Chaojie Gu, Yuanchao Shu, <strong>Cong Wang*</strong><br>
<em>The 19th European Conference on Computer Vision</em> <a href="https://github.com/JingqiJi03/AEGIS" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/code--%20?style=social&logo=github" alt="code link"></a> <a href="/files/eccv26_a.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ECCV 26</span></div>
  <div class="pub-body"><p>Vision-TTT: Efficient and Expressive Visual Representation Learning with Test-Time Training<br>
Quan Kong, Yanru Xiao, Yuhao Shen, <strong>Cong Wang*</strong><br>
<em>The 19th European Conference on Computer Vision</em> <a href="https://arxiv.org/abs/2603.00518" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ACL 26</span></div>
  <div class="pub-body"><p>Double: Breaking the Acceleration Limit via Double Retrieval Speculative Parallelism <span class="award-badge award-candidate">🏆 Best Paper Candidate</span><br>
Yuhao Shen, Tianyu Liu, Junyi Shen, Jinyang Wu, Quan Kong, Huan Li, <strong>Cong Wang*</strong><br>
<em>The 64th Annual Meeting of the Association for Computational Linguistics (Best Paper Candidate) </em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ACL 26</span></div>
  <div class="pub-body"><p>See the Forest for the Trees: Loosely Speculative Decoding via Visual-Semantic Guidance for Efficient Inference of Video LLMs<br>
Yicheng Ji, Jun Zhang, Jinpeng Chen, <strong>Cong Wang</strong>, Lidan Shou, Gang Chen, Huan Li<br>
<em>The 64th Annual Meeting of the Association for Computational Linguistics (Oral)</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">SIGIR 26</span></div>
  <div class="pub-body"><p>Denoise and Align: Diffusion-Driven Foreground Knowledge Prompting for Open-Vocabulary Temporal Action Detection<br>
Sa Zhu, Wanqian Zhang, Lin Wang, Jinchao Zhang, <strong>Cong Wang</strong>, Bo Li<br>
<em>The 49th International ACM SIGIR Conference on Research and Development in Information Retrieval</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">CVPR 26</span></div>
  <div class="pub-body"><p>ParallelVLM: Lossless Video-LLM Acceleration with Visual Alignment Aware Parallel Speculative Decoding<br>
Quan Kong, Yuhao Shen, Yicheng Ji, Huan Li, <strong>Cong Wang*</strong><br>
<em>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Denvor, CO, USA</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ICLR 26</span></div>
  <div class="pub-body"><p>SpecBranch: Speculative Decoding via Hybrid Drafting and Rollback-Aware Branch Parallelism<br>
Yuhao Shen, Junyi Shen, Quan Kong, Tianyu Liu, Yao Lu, <strong>Cong Wang*</strong><br>
<em>The International Conference on Learning Representations, Rio De Janeiro, Brazil</em> <a href="https://github.com/Sylvan820/Specbranch" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/code--%20?style=social&logo=github" alt="code link"></a> <a href="/files/iclr26.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ICSE 26</span></div>
  <div class="pub-body"><p>End-to-End Model Generation with Large Language Models for Adaptive IoT Application Deployment<br>
Zhenyu Wen, Jintao Feng, Nanjie Yao, Di Wu, <strong>Cong Wang</strong>, Mincheng Wu, Jianbin Qin, Shibo He<br>
<em>48th IEEE/ACM International Conference on Software Engineering</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">AAAI 26</span></div>
  <div class="pub-body"><p>Beyond Single-Point Perturbation: A Hierarchical, Manifold-Aware Approach to Diffusion Attacks<br>
Zhijie Wang, Lin Wang, Zhenyu Wen, <strong>Cong Wang*</strong><br>
<em>The 40th Annual AAAI Conference on Artificial Intelligence, Singapore</em> <a href="https://github.com/wa789w/HAM" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/code--%20?style=social&logo=github" alt="code link"></a> <a href="/files/aaai26b.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">AAAI 26</span></div>
  <div class="pub-body"><p>RFF-TTA: Physical Information-Aware Prototype for Temporally Varying RF Fingerprinting Online Test-Time-Adaptation<br>
Taotao Li, Yiyang Li, Zhenyu Wen, Jiahao Lin, Jinhao Wan, Jie Su, <strong>Cong Wang</strong>, Zhen Hong<br>
<em>The 40th Annual AAAI Conference on Artificial Intelligence, Singapore (Oral)</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">CVPR 25</span></div>
  <div class="pub-body"><p>Can't Slow me Down: Learning Robust and Hardware-Adaptive Object Detectors against Latency Attacks for Edge Devices<br>
Tianyi Wang, Zichen Wang, <strong>Cong Wang*</strong>, Yuanchao Shu, Ruilong Deng, Peng Cheng, Jiming Chen<br>
<em>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Nashville TN, USA</em> <a href="https://github.com/Hill-Wu-1998/underload" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/code--%20?style=social&logo=github" alt="code link"></a> <a href="/files/cvpr25.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">AAAI 25</span></div>
  <div class="pub-body"><p>Fed-DFA: Federated Distillation for Heterogeneous Model Fusion through the Adversarial Lens<br>
Zichen Wang, Feng Yan, Tianyi Wang, <strong>Cong Wang*</strong>, Yuanchao Shu, Peng Cheng, Jiming Chen<br>
<em>The 39th Annual AAAI Conference on Artificial Intelligence, Philadelphia, PA, USA</em> <a href="/files/aaai25.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ACM MM 25</span></div>
  <div class="pub-body"><p>DeCoRec: Decoupled Collaborative Refinement for Multi-Modal Sequential Recommendations<br>
Zhaoqi Chen, Wanni Xu, Yunfeng Zhang, Yawei Hou, Zhenyu Wen, <strong>Cong Wang*</strong><br>
<em>ACM Multimedia Conference, Dublin, Ireland, 2025</em> <a href="https://github.com/KIKIENAO/decorec" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/code--%20?style=social&logo=github" alt="code link"></a> <a href="/files/mm25.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">KDD 25</span></div>
  <div class="pub-body"><p>FLMarket: Enabling Privacy-preserved Pre-training Data Pricing for Federated Learning<br>
Zhenyu Wen, Wanglei Feng, Di Wu*, Haozhen Hu, Chang Xu, Bin Qian, Zhen Hong, <strong>Cong Wang*</strong>, Shouling Ji<br>
<em>ACM SIGKDD Conference on Knowledge Discovery and Data Mining</em> <a href="https://www.youtube.com/watch?v=GNJfaPAP5K8" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/video--%20?style=social&logo=youtube" alt="video link"></a> <a href="https://arxiv.org/pdf/2411.11713" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ICDCS 25</span></div>
  <div class="pub-body"><p>Hetero<sup>2</sup>Pipe: Pipelining Multi-DNN Inference on Heterogeneous Mobile Processors under Co-Execution Slowdown<br>
Yuhao Shen, Zichen Wang, Tianyi Wang, Chaojie Gu, Zhenyu Wen, Yuanchao Shu, <strong>Cong Wang*</strong><br>
<em>IEEE International Conference on Distributed Computing Systems, Glasgow, UK, 2025</em> <a href="/files/icdcs25.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">IWQoS 24</span></div>
  <div class="pub-body"><p>Heterogeneity-aware memory efficient federated learning via progressive layer freezing<br>
Yebo Wu, Li Li, Chunlin Tian, Tao Chang, Chi Lin, <strong>Cong Wang</strong>, Cheng-Zhong Xu<br>
<em>IEEE/ACM 32nd International Symposium on Quality of Service (IWQoS), 2024</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">SecureComm 23</span></div>
  <div class="pub-body"><p>Unsupervised Multi-Criteria Adversarial Detection in Deep Image Retrieval<br>
Yanru Xiao, <strong>Cong Wang*</strong>, Xing Gao<br>
<em>International Conference on Security and Privacy in Communication Systems, 2023</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ICDCS 22</span></div>
  <div class="pub-body"><p>Energy Minimization for Federated Asynchronous Learning on Battery-Powered Mobile Devices via Application Co-running<br>
<strong>Cong Wang*</strong>, Bin Hu and Hongyi Wu<br>
<em>IEEE International Conference on Distributed Computing Systems, 2022</em> <a href="/files/icdcs22.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">CVPR 21</span></div>
  <div class="pub-body"><p>You See What I Want You to See: Exploring Targeted Black-Box Transferability Attack for Hash-based Image Retrieval Systems<br>
Yanru Xiao, <strong>Cong Wang*</strong><br>
<em>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2021</em> <a href="https://github.com/SugarRuy/CVPR21_Transferred_Hash" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/code--%20?style=social&logo=github" alt="code link"></a> <a href="https://openaccess.thecvf.com/content/CVPR2021/papers/Xiao_You_See_What_I_Want_You_To_See_Exploring_Targeted_CVPR_2021_paper.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">CVPR 20</span></div>
  <div class="pub-body"><p>Evade Deep Image Retrieval by Stashing Private Images in the Hash Space<br>
Yanru Xiao, <strong>Cong Wang*</strong>, Xing Gao<br>
<em>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020</em> <a href="https://github.com/SugarRuy/HashStash" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/code--%20?style=social&logo=github" alt="code link"></a> <a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiao_Evade_Deep_Image_Retrieval_by_Stashing_Private_Images_in_the_CVPR_2020_paper.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ACM MM 20</span></div>
  <div class="pub-body"><p>Gangsweep: Sweep out neural backdoors by gan<br>
Liuwan Zhu, Rui Ning, <strong>Cong Wang</strong>, Chunsheng Xin, Hongyi Wu<br>
<em>Proceedings of the 28th ACM International Conference on Multimedia, 2020</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">INFOCOM 20</span></div>
  <div class="pub-body"><p>Design and Optimization of Electric Autonomous Vehicles with Renewable Energy Source for Smart Cities<br>
Pengzhan Zhou, <strong>Cong Wang and Yuanyuan Yang</strong><br>
<em>IEEE Conference on Computer Communications, Toronto, ON, Canada, 2020</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">IPDPS 20</span></div>
  <div class="pub-body"><p>Optimize Scheduling of Federated Learning on Battery-powered Mobile Devices<br>
<strong>Cong Wang*</strong>, Xin Wei and Pengzhan Zhou<br>
<em>IEEE International Parallel and Distributed Processing Symposium (IPDPS), New Orleans, LA, USA, 2020</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ICDCS 20</span></div>
  <div class="pub-body"><p>E-Sharing: Data-driven Online Optimization of Parking Location Placement for Dockless Electric Bike Sharing<br>
Pengzhan Zhou, Xin Wei, <strong>Cong Wang* and Yuanyuan Yang*</strong><br>
<em>International Conference on Distributed Computing Systems (ICDCS), Singapore, 2020</em> <a href="https://colinzpz.github.io/files/icdcs20.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">IJCAI 19</span></div>
  <div class="pub-body"><p>Explore Truthful Incentives for Tasks with Heterogenous Levels of Difficulty in the Sharing Economy<br>
Pengzhan Zhou, Xin Wei, <strong>Cong Wang* and Yuanyuan Yang*</strong><br>
<em>Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence</em> <a href="https://www.ijcai.org/proceedings/2019/0094.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ACM MM 19</span></div>
  <div class="pub-body"><p>Close the Gap between Deep Learning and Mobile Intelligence by Incorporating Training in the Loop<br>
<strong>Cong Wang*</strong>, Yanru Xiao, Xing Gao, Li Li, Jun Wang<br>
<em>Proceedings of the 27th ACM International Conference on Multimedia, 2019</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">CCS 19</span></div>
  <div class="pub-body"><p>Houdini’s Escape: Breaking the Resource Rein of Linux Control Groups<br>
Xing Gao, Zhongshu Gu, Zhengfa Li, Hani Jamjoom, <strong>Cong Wang</strong><br>
<em>ACM Conference on Computer and Communications Security (CCS), London, UK, 2019</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">INFOCOM 19</span></div>
  <div class="pub-body"><p>CapJack: Capture In-Browser Crypto-jacking by Deep Capsule Network through Behavioral Analysis<br>
Rui Ning, <strong>Cong Wang</strong>, Chunsheng Xin, Jiang Li, Liuwan Zhu and Hongyi Wu<br>
<em>IEEE Conference on Computer Communications, Paris, France, 2019</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">INFOCOM 19</span></div>
  <div class="pub-body"><p>Self-sustainable Sensor Networks with Multi-source Energy Harvesting and Wireless Charging<br>
Pengzhan Zhou, <strong>Cong Wang</strong>, Yuanyuan Yang<br>
<em>IEEE Conference on Computer Communications, Paris, France, 2019</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">IJCAI 18</span></div>
  <div class="pub-body"><p>GELU-Net: A Globally Encrypted, Locally Unencrypted Deep Neural Network for Privacy-Preserved Learning<br>
Qiao Zhang, <strong>Cong Wang</strong>, Hongyi Wu, Chunsheng Xin, Tran V Phuong<br>
<em>Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence</em> <a href="https://www.ijcai.org/Proceedings/2018/0547.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">PerCom 18</span></div>
  <div class="pub-body"><p>DeepMag: Sniffing Mobile Apps in Magnetic Field through Deep Convolutional Neural Networks <span class="award-badge award-winner">🥇 Mark Weiser Best Paper Award</span><br>
Rui Ning, <strong>Cong Wang</strong>, Chunsheng Xin, Jiang Li and Hongyi Wu<br>
<em>IEEE International Conference on Pervasive Computing and Communications (PerCom), Athens, Greece, 2018</em></p></div>
</li>
</ul>

<button class="fold-toggle" onclick="toggleFold(this, 'conf-old')">
  <span class="fold-arrow">▼</span>
  Earlier work — PhD period (2010–2017)
  <span class="fold-count">8 papers</span>
</button>
<div class="fold-content" id="conf-old">
<ul class="pub-list">
<li>
  <div class="pub-tag"><span class="pub-badge conf">ICDCS 17</span></div>
  <div class="pub-body"><p>Leveraging Target k-Coverage in Wireless Rechargeable Sensor Network<br>
Pengzhan Zhou, <strong>Cong Wang and Yuanyuan Yang</strong><br>
<em>IEEE International Conference on Distributed Computing Systems, Atlanta, GA, 2017</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ICDCS 17</span></div>
  <div class="pub-body"><p>Design and Implementation of a Versatile Platform for Mobile Data Gathering in Wireless Sensor Networks<br>
Ji Li, <strong>Cong Wang and Yuanyuan Yang</strong><br>
<em>IEEE International Conference on Distributed Computing Systems, Atlanta, GA, 2017</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">INFOCOM 16</span></div>
  <div class="pub-body"><p>A Hybrid Framework Combining Solar Energy Harvesting and Wireless Charging for Wireless Sensor Networks<br>
<strong>Cong Wang</strong>, Ji Li, Yuanyuan Yang and Fan Ye<br>
<em>IEEE International Conference on Computer Communications, San Francisco, CA, 2016</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ICDCS 15</span></div>
  <div class="pub-body"><p>Improve Charging Capability for Wireless Rechargeable Sensor Networks using Resonant Repeaters<br>
<strong>Cong Wang</strong>, Ji Li, Fan Ye and Yuanyuan Yang<br>
<em>IEEE International Conference on Distributed Computing Systems, Columbus, OH, 2015</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">ICPP 15</span></div>
  <div class="pub-body"><p>Joint Wireless Charging and Sensor Activity Management in Wireless Rechargeable Sensor Networks<br>
Yuan Gao, <strong>Cong Wang and Yuanyuan Yang</strong><br>
<em>IEEE International Conference on Parallel Processing, Beijing, China, 2015</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">SECON 14</span></div>
  <div class="pub-body"><p>Recharging Schedules for Wireless Sensor Networks with Vehicle Movement Costs and Capacity Constraints<br>
<strong>Cong Wang</strong>, Ji Li, Fan Ye and Yuanyuan Yang<br>
<em>IEEE International Conference on Sensing Communication and Networking (IEEE SECON), Singapore, 2014</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">INFOCOM 13</span></div>
  <div class="pub-body"><p>Mobile Data Gathering with Wireless Energy Replenishment in Rechargeable Sensor Networks<br>
Songtao Guo, <strong>Cong Wang and Yuanyuan Yang</strong><br>
<em>IEEE International Conference on Computer Communications, Turin, Italy, 2013</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge conf">IPDPS 13</span></div>
  <div class="pub-body"><p>Multi-Vehicle Coordination for Wireless Energy Replenishment in Sensor Networks<br>
<strong>Cong Wang</strong>, Ji Li, Fan Ye, Yuanyuan Yang<br>
<em>IEEE 27th International Symposium on Parallel and Distributed Processing (IPDPS)</em></p></div>
</li>
</ul>
</div>

<h2 class="section-title" style="margin-top:2.5em">Selected Journal Publications</h2>

<ul class="pub-list">
<li>
  <div class="pub-tag"><span class="pub-badge jour">TIFS 26</span></div>
  <div class="pub-body"><p>The Chosen-Object Attack: Exploiting the Hungarian Matching Loss in Detection Transformers for Fun and Profit<br>
Tianyi Wang, <strong>Cong Wang*</strong>, Zhenyu Wen, Ruilong Deng, Yuanchao Shu, Peng Cheng, Jiming Chen<br>
<em>IEEE Transactions on Information Forensics and Security</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">THMS 25</span></div>
  <div class="pub-body"><p>Human Perception of AI Capabilities at Classifying Perturbed Roadway Signs<br>
Katherine R Garcia, Jing Chen, Yanru Xiao, Scott Mishler, <strong>Cong Wang</strong>, Bin Hu<br>
<em>IEEE Transactions on Human-Machine Systems</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TNNLS 25</span></div>
  <div class="pub-body"><p>SENGraph: A Self-Learning Evolutionary and Node-Aware Graph Network for Soft Sensing in Industrial Processes<br>
Feng Yan, <strong>Cong Wang</strong>, Zichen Wang, Yuhao Shen, Chunjie Yang<br>
<em>IEEE Transactions on Neural Networks and Learning Systems</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TMC 24</span></div>
  <div class="pub-body"><p>Energy Optimization for Federated Learning on Consumer Mobile Devices With Asynchronous SGD and Application Co-Execution<br>
<strong>Cong Wang</strong>, Hongyi Wu<br>
<em>IEEE Transactions on Mobile Computing</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">ACM TOIT 24</span></div>
  <div class="pub-body"><p>Efficient Vertical Federated Unlearning via Fast Retraining<br>
Zichen Wang, Xiangshan Gao, <strong>Cong Wang</strong>, Peng Cheng, Jiming Chen<br>
<em>ACM Transactions on Internet Technology</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">JPDC 24</span></div>
  <div class="pub-body"><p>PerfTop: Towards performance prediction of distributed learning over general topology<br>
Changzhi Yan, Zehan Zhu, Youcheng Niu, <strong>Cong Wang</strong>, Cheng Zhuo, Jinming Xu<br>
<em>Journal of Parallel and Distributed Computing</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TMC 23</span></div>
  <div class="pub-body"><p>A Framework for Behavioral Biometric Authentication using Deep Metric Learning on Mobile Devices<br>
<strong>Cong Wang</strong>, Yanru Xiao, Xing Gao, Li Li, Jun Wang<br>
<em>IEEE Transactions on Mobile Computing</em> <a href="paper/tmc23.pdf" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TMC 23</span></div>
  <div class="pub-body"><p>Design and Optimization of Solar-Powered Shared Electric Autonomous Vehicle System for Smart Cities<br>
Pengzhan Zhou, <strong>Cong Wang</strong>, Yuanyuan Yang<br>
<em>IEEE Transactions on Mobile Computing</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TOSN 22</span></div>
  <div class="pub-body"><p>Economical behavior modeling and analyses for data collection in edge Internet of Things networks<br>
Yiming Zeng, Pengzhan Zhou, <strong>Cong Wang</strong>, Ji Liu, Yuanyuan Yang<br>
<em>ACM Transactions on Sensor Networks</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TPDS 21</span></div>
  <div class="pub-body"><p>Towards Efficient Scheduling of Federated Mobile Devices under Computational and Statistical Heterogeneity <span class="award-badge award-candidate">🏆 Best Paper Candidate</span><br>
<strong>Cong Wang</strong>, Yuanyuan Yang, Pengzhan Zhou<br>
<em>IEEE Transactions on Parallel and Distributed Systems</em> <a href="https://arxiv.org/abs/2005.12326" style="text-decoration: none; margin-left: 5px;"><img src="https://img.shields.io/badge/paper--%20?style=social&logo=arxiv" alt="paper link"></a></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TC 21</span></div>
  <div class="pub-body"><p>K-level truthful incentivizing mechanism and generalized k-MAB problem<br>
Pengzhan Zhou, Xin Wei, <strong>Cong Wang</strong>, Yuanyuan Yang<br>
<em>IEEE Transactions on Computers</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TOSN 21</span></div>
  <div class="pub-body"><p>Design of Self-sustainable Wireless Sensor Networks with Energy Harvesting and Wireless Charging<br>
Pengzhan Zhou, <strong>Cong Wang</strong>, Yuanyuan Yang<br>
<em>ACM Transactions on Sensor Networks</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TMC 19</span></div>
  <div class="pub-body"><p>Static and Mobile Target k-Coverage in Wireless Rechargeable Sensor Networks<br>
Pengzhan Zhou, <strong>Cong Wang</strong>, Yuanyuan Yang<br>
<em>IEEE Transactions on Mobile Computing</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TMC 18</span></div>
  <div class="pub-body"><p>Combining Solar Energy Harvesting with Wireless Charging for Hybrid Wireless Sensor Networks<br>
<strong>Cong Wang</strong>, Ji Li, Yuanyuan Yang, Fan Ye<br>
<em>IEEE Transactions on Mobile Computing</em></p></div>
</li>
</ul>

<button class="fold-toggle" onclick="toggleFold(this, 'jour-old')">
  <span class="fold-arrow">▼</span>
  Earlier work — PhD period (2010–2017)
  <span class="fold-count">7 papers</span>
</button>
<div class="fold-content" id="jour-old">
<ul class="pub-list">
<li>
  <div class="pub-tag"><span class="pub-badge jour">TMC 17</span></div>
  <div class="pub-body"><p>A Novel Framework of Multi-Hop Wireless Charging for Sensor Networks Using Resonant Repeaters<br>
<strong>Cong Wang</strong>, Ji Li, Fan Ye, Yuanyuan Yang<br>
<em>IEEE Transactions on Mobile Computing</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TMC 16</span></div>
  <div class="pub-body"><p>An Optimization Framework for Mobile Data Collection in Energy-Harvesting Wireless Sensor Networks<br>
<strong>Cong Wang</strong>, Songtao Guo, Yuanyuan Yang<br>
<em>IEEE Transactions on Mobile Computing</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TC 16</span></div>
  <div class="pub-body"><p>A Mobile Data Gathering Framework for Wireless Rechargeable Sensor Networks with Vehicle Movement Costs and Capacity Constraints<br>
<strong>Cong Wang</strong>, Ji Li, Fan Ye, Yuanyuan Yang<br>
<em>IEEE Transactions on Computers</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TMC 16</span></div>
  <div class="pub-body"><p>DaGCM: A Concurrent Data Uploading Framework for Mobile Data Gathering in Wireless Sensor Networks<br>
Songtao Guo, Yuanyuan Yang, <strong>Cong Wang</strong><br>
<em>IEEE Transactions on Mobile Computing</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TMC 15</span></div>
  <div class="pub-body"><p>Mobile Data Gathering with Load Balanced Clustering and Dual Data Uploading in Wireless Sensor Networks<br>
Miao Zhao, Yuanyuan Yang, <strong>Cong Wang</strong><br>
<em>IEEE Transactions on Mobile Computing</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TMC 14</span></div>
  <div class="pub-body"><p>NETWRAP: An NDN Based Real-TimeWireless Recharging Framework for Wireless Sensor Networks<br>
<strong>Cong Wang</strong>, Ji Li, Fan Ye, Yuanyuan Yang<br>
<em>IEEE Transactions on Mobile Computing</em></p></div>
</li>
<li>
  <div class="pub-tag"><span class="pub-badge jour">TMC 14</span></div>
  <div class="pub-body"><p>Joint Mobile Data Gathering and Energy Provisioning in Wireless Rechargeable Sensor Networks<br>
Songtao Guo, <strong>Cong Wang</strong>, Yuanyuan Yang<br>
<em>IEEE Transactions on Mobile Computing</em></p></div>
</li>
</ul>
</div>

</div>
