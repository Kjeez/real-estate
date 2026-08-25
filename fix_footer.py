import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

correct_footer = '''  <!-- ============ FOOTER ============ -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="logo-text">DHOLERA</div>
          <span class="logo-subtitle">Real Estate</span>
          <p>The information presented on this website is intended for general informational purposes only. Property availability, pricing, specifications, approvals, infrastructure timelines and other project information may change. Nothing on this website should be interpreted as a guarantee of property appreciation, rental income or investment returns.</p>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="why-dholera.html">Dholera SIR</a></li>
            <li><a href="projects.html">Projects</a></li>
            <li><a href="location.html">Location</a></li>
            <li><a href="infrastructure.html">Infrastructure</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Explore</h4>
          <ul>
            <li><a href="residential.html">Residential</a></li>
            <li><a href="commercial-industrial.html">Commercial & Industrial</a></li>
            <li><a href="why-choose-us.html">Why Us</a></li>
            <li><a href="how-it-works.html">How It Works</a></li>
            <li><a href="nri.html">NRI Investment</a></li>
            <li><a href="faqs.html">FAQs</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contact Us</h4>
          <ul>
            <li><a href="mailto:info@dholerarealstate.com">info@dholerarealstate.com</a></li>
            <li><a href="tel:+91XXXXXXXXXX">+91 XXXXX XXXXX</a></li>
            <li>Ahmedabad, Gujarat, India</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 Dholera Real Estate. All Rights Reserved.</p>
      </div>
    </div>
  </footer>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The footer can start with <!-- ============ FOOTER ============ -->
    # or just <footer class="footer">
    # Let's replace everything from <footer class="footer"> to </footer>
    
    # Let's find if there's a comment before the footer.
    # We will replace from <footer class="footer"> to </footer> with the core footer block.
    # (Without the comment if it's already there)
    
    footer_pattern = re.compile(r'<footer class="footer">.*?</footer>', re.DOTALL)
    
    core_footer = correct_footer.split('<!-- ============ FOOTER ============ -->\n')[1]
    
    if footer_pattern.search(content):
        content = footer_pattern.sub(core_footer, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Footer corrected in all HTML files.")
