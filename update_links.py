import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Standard Navigation Block
new_nav = '''      <div class="nav-links" id="navLinks">
        <a href="index.html">Home</a>
        <a href="about.html">About Us</a>
        <a href="why-dholera.html">Dholera SIR</a>
        <a href="projects.html">Projects</a>
        <a href="why-choose-us.html">Why Us</a>
        <a href="faqs.html">FAQs</a>
        <a href="contact.html">Contact</a>
      </div>'''

# Standard Footer Links (Cols 1 & 2)
new_footer_links = '''        <div class="footer-col">
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
        </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Nav Links
    # Uses regex to match <div class="nav-links" id="navLinks"> ... </div>
    # dotall flag allows . to match newlines
    nav_pattern = re.compile(r'      <div class="nav-links" id="navLinks">.*?</div>', re.DOTALL)
    content = nav_pattern.sub(new_nav, content)

    # Replace Footer Columns
    # The footer has multiple columns. We want to replace the first two <div class="footer-col"> blocks.
    # To be safe, we'll find <div class="footer-brand">...</div> and the next <div class="footer-col">...</div> (Contact us)
    # and replace everything in between.
    
    # Or, an easier way: find the footer-brand closing tag and the Contact Us h4, and replace what's between.
    footer_pattern = re.compile(r'(<div class="footer-brand">.*?</div>\s*)(<div class="footer-col">.*?)(<div class="footer-col">\s*<h4>Contact Us</h4>)', re.DOTALL)
    
    # We only have "Contact Us" in the footer on some pages. Let's check if the pattern matches.
    if footer_pattern.search(content):
         content = footer_pattern.sub(r'\1' + new_footer_links + r'\n        \3', content)
    else:
        # Some pages don't have the full footer we built in index.html, they have abbreviated footers.
        # Let's replace whatever is between <div class="footer-brand">...</div> and </div>\s*<div class="footer-bottom">
        footer_pattern2 = re.compile(r'(<div class="footer-brand">.*?</div>\s*)(.*?)(</div>\s*<div class="footer-bottom">)', re.DOTALL)
        content = footer_pattern2.sub(r'\1' + new_footer_links + r'\n      \3', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated links in all HTML files.")
