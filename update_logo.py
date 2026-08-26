import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll replace the `.logo-icon` div with the image.
logo_pattern = re.compile(r'<div class="logo-icon">\s*<svg.*?</svg>\s*</div>', re.DOTALL)
new_logo = '<img src="images/golden%20key%20png.png" alt="Logo" class="logo-icon-img">'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if logo_pattern.search(content):
        content = logo_pattern.sub(new_logo, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Logo updated in all HTML files.")
