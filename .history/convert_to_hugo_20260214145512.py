import os
import re

root = "/Users/wangwei69/VisualCode/blog/dancvv.github.io"
output_dir = os.path.join(root, "content", "posts")
os.makedirs(output_dir, exist_ok=True)

dirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
hugo_dirs = []

# Exclude obvious non-content dirs
exclude = {'css', 'js', 'lib', 'images', 'page', 'categories', 'tags', 'posts', 'svg'}

for d in dirs:
    if d in exclude or d.startswith('.'): continue
    path = os.path.join(root, d)
    if os.path.exists(os.path.join(path, "index.html")) and os.path.exists(os.path.join(path, "index.md")):
        hugo_dirs.append(d)

print(f"Found {len(hugo_dirs)} directories: {hugo_dirs}")

for d in hugo_dirs:
    html_path = os.path.join(root, d, "index.html")
    md_path = os.path.join(root, d, "index.md")
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    title_match = re.search(r'<meta property="og:title" content="(.*?)" />', html_content)
    title = title_match.group(1) if title_match else d
    
    # Remove site title suffix if present (e.g. " - My Blog")
    if " - " in title:
        title = title.split(" - ")[0]

    date_match = re.search(r'<meta property="article:published_time" content="(.*?)" />', html_content)
    date = date_match.group(1) if date_match else ""

    desc_match = re.search(r'<meta property="og:description" content="(.*?)" />', html_content)
    description = desc_match.group(1) if desc_match else ""
    
    # Try to extract tags/categories if possible.
    # Often Hugo themes put tags in meta keywords
    tags = []
    # Check for meta property="article:tag"
    p_tags = re.findall(r'<meta property="article:tag" content="(.*?)" />', html_content)
    if p_tags:
        tags.extend(p_tags)
        
    keywords_match = re.search(r'<meta name="keywords" content="(.*?)" />', html_content)
    if keywords_match:
        k_tags = [k.strip() for k in keywords_match.group(1).split(',')]
        for k in k_tags:
            if k not in tags:
                tags.append(k)

    # Read markdown content
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
    else:
        md_content = ""

    # Frontmatter construction
    frontmatter = "+++\n"
    # Clean up title: remove HTML entities if any
    title = title.replace("&quot;", '"').replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    
    frontmatter += f'title = "{title}"\n'
    if date:
        date = date.strip()
        frontmatter += f'date = "{date}"\n'
    if description:
        # Escape quotes in description just in case
        description = description.replace('"', '\\"').replace('\n', ' ')
        frontmatter += f'description = "{description}"\n'
    if tags:
        # Format tags as TOML array strings
        tags_str = ", ".join([f'"{t}"' for t in tags if t])
        frontmatter += f'tags = [{tags_str}]\n'
        
    frontmatter += "+++\n\n"
    
    # Remove H1 if it duplicates title (simple heuristic)
    lines = md_content.split('\n')
    if lines and lines[0].strip().startswith('# ') and title.lower() in lines[0].lower():
        md_content = '\n'.join(lines[1:])
    
    new_content = frontmatter + md_content
    
    output_path = os.path.join(output_dir, f"{d}.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Created {output_path}")
