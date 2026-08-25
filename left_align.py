import os
import re

css_dir = 'css'

# Files to check
css_files = [os.path.join(css_dir, f) for f in os.listdir(css_dir) if f.endswith('.css')]

for file in css_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update .page-hero-content
    # Find block .page-hero-content { ... }
    # Inside it, replace text-align: center with text-align: left, and margin: 0 auto with margin: 0
    content = re.sub(r'(\.page-hero-content\s*\{[^}]*)text-align:\s*center;([^}]*\})', r'\1text-align: left;\2', content)
    content = re.sub(r'(\.page-hero-content\s*\{[^}]*)margin:\s*0\s*auto;([^}]*\})', r'\1margin: 0;\2', content)

    # 2. Update .page-header-simple
    content = re.sub(r'(\.page-header-simple\s*\{[^}]*)text-align:\s*center;([^}]*\})', r'\1text-align: left;\2', content)
    content = re.sub(r'(\.page-header-simple\s*p\s*\{[^}]*)margin:\s*0\s*auto;([^}]*\})', r'\1margin: 0;\2', content)

    # 3. Update .hero-content (in style.css)
    content = re.sub(r'(\.hero-content\s*\{[^}]*)text-align:\s*center;([^}]*\})', r'\1text-align: left;\2', content)
    content = re.sub(r'(\.hero-content\s*\{[^}]*)margin:\s*0\s*auto;([^}]*\})', r'\1margin: 0;\2', content)

    # 4. Update .hero-buttons (in style.css)
    # Ensure they align left if they are flex
    # Actually, they default to flex-start anyway unless specified. Let's make sure.
    content = re.sub(r'(\.hero-buttons\s*\{[^}]*)justify-content:\s*center;([^}]*\})', r'\1justify-content: flex-start;\2', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated CSS to left-align hero banners.")
