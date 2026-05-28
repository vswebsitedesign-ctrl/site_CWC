#!/usr/bin/env python3
import json, os, shutil, sys, re

def build():
    pages_path = 'data/pages.json'
    if not os.path.exists(pages_path):
        print("ERROR: pages.json not found")
        sys.exit(1)
    with open(pages_path, 'r') as f:
        pages = json.load(f)
    with open('theme/base.html', 'r') as f:
        template = f.read()

    if os.path.exists('build'):
        shutil.rmtree('build')
    os.makedirs('build')

    BASE_URL = 'https://cornwallwasteclearance.co.uk'

    for page in pages:
        slug = page.get('slug', '')
        title = page.get('title', '')
        description = page.get('description', '')
        canonical = f"{BASE_URL}/{slug}/" if slug else f"{BASE_URL}/"
        robots = page.get('robots', 'index, follow')

        content = page.get('body_content', '')
        # Strip any raw Liquid/Jekyll template tags left in content
        content = re.sub(r'\{%.*?%\}', '', content, flags=re.DOTALL)
        content = re.sub(r'\{\{.*?\}\}', '', content, flags=re.DOTALL)

        html = template
        html = html.replace('<title></title>', f'<title>{title}</title>')
        html = html.replace('content="noindex, follow"', f'content="{robots}"')
        html = html.replace('<meta name="description" content="">', f'<meta name="description" content="{description}">')
        html = html.replace('<link rel="canonical" href="" />', f'<link rel="canonical" href="{canonical}" />')
        html = html.replace('<meta property="og:title" content="" />', f'<meta property="og:title" content="{title}" />')
        html = html.replace('<meta property="og:description" content="" />', f'<meta property="og:description" content="{description}" />')
        html = html.replace('<meta property="og:url" content="" />', f'<meta property="og:url" content="{canonical}" />')
        html = html.replace('{{ content }}', content)

        out_dir = os.path.join('build', slug) if slug else 'build'
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, 'index.html'), 'w') as f:
            f.write(html)

    if os.path.exists('assets'):
        shutil.copytree('assets', 'build/assets', dirs_exist_ok=True)
    print(f"Built {len(pages)} pages")

if __name__ == '__main__':
    build()
