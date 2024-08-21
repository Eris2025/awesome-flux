import markdown
from jinja2 import Template
import re
from bs4 import BeautifulSoup

# Read the README.md file
with open('README.md', 'r') as f:
    readme_content = f.read()

# Convert Markdown to HTML using python-markdown
html_content = markdown.markdown(readme_content, extensions=['extra', 'toc'])

# Modify HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Add target and rel attributes to external links
for a in soup.find_all('a', href=True):
    if not a['href'].startswith('#'):
        a['target'] = '_blank'
        a['rel'] = 'noopener noreferrer'

# Ensure proper nesting of list items in the table of contents
toc = soup.find('div', class_='toc')
if toc:
    current_level = 0
    current_ul = None
    for li in toc.find_all('li', recursive=False):
        level = int(li.get('class', ['level1'])[0].replace('level', ''))
        if level > current_level:
            new_ul = soup.new_tag('ul')
            if current_ul:
                current_ul.append(new_ul)
            else:
                li.wrap(new_ul)
            current_ul = new_ul
        elif level < current_level:
            current_ul = current_ul.parent
        current_level = level
        current_ul.append(li)

html_content = str(soup)

# Extract the first paragraph as description
description = re.search(r'<p>(.*?)</p>', html_content, re.DOTALL)
description = description.group(
    1) if description else "A curated list of awesome resources for Flux AI image generation model."

# Create an optimized HTML template with beautified CSS and JavaScript
template = Template('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Awesome Flux AI | Curated Resources for Flux AI Image Generation Model</title>
    <meta name="description" content="{{ description }}">
    <meta name="keywords" content="Flux AI, image generation, AI model, machine learning, deep learning, awesome flux">
    <meta name="author" content="Awesome Flux AI Community">
    <link rel="canonical" href="https://awesomeflux.com">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1, h2 {
            color: #2c3e50;
        }
        h1 {
            font-size: 2.5em;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            font-size: 1.8em;
            margin-top: 30px;
        }
        a {
            color: #3498db;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        a:hover {
            color: #2980b9;
            text-decoration: underline;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
        header {
            margin-bottom: 30px;
        }
        footer {
            margin-top: 30px;
            text-align: center;
            font-size: 0.9em;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <main>
            {{ content }}
        </main>
        <footer>
            <p>© 2024 AwesomeFlux.com. All rights reserved.</p>
        </footer>
    </div>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Awesome Flux AI",
      "description": "{{ description }}",
      "url": "https://awesomeflux.com"
    }
    </script>
    <script>
    document.addEventListener('DOMContentLoaded', (event) => {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            });
        });
    });
    </script>
</body>
</html>
''')

# Render HTML
output = template.render(content=html_content, description=description)

# Write the generated HTML to a file
with open('index.html', 'w') as f:
    f.write(output)

print("Website for awesomeflux generated successfully!")
