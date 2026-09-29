from pathlib import Path
from html import unescape
import re
import subprocess
from xml.etree.ElementTree import Element, SubElement, ElementTree, register_namespace

ROOT = Path(__file__).resolve().parents[1]
INDEX_FILES = [ROOT / "index.html"] + sorted(ROOT.glob("*/index.html")) + sorted(ROOT.glob("*/*/index.html"))

def text(path):
    return path.read_text(encoding="utf-8")

def canonical(html):
    m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', html, re.I)
    if not m:
        m = re.search(r'<link\s+href=["\']([^"\']+)["\']\s+rel=["\']canonical["\']', html, re.I)
    return unescape(m.group(1)) if m else None

def noindex(html):
    m = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\']([^"\']+)["\']', html, re.I)
    return bool(m and "noindex" in m.group(1).lower())

def lastmod(path):
    rel = path.relative_to(ROOT).as_posix()
    try:
        value = subprocess.check_output(
            ["git", "log", "-1", "--format=%cs", "--", rel],
            cwd=ROOT,
            text=True
        ).strip()
        return value or None
    except Exception:
        return None

urls = []
for path in INDEX_FILES:
    html = text(path)
    if noindex(html):
        continue
    url = canonical(html)
    if not url:
        continue
    urls.append((url, lastmod(path)))

register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
urlset = Element("{http://www.sitemaps.org/schemas/sitemap/0.9}urlset")
for url, modified in sorted(set(urls)):
    node = SubElement(urlset, "{http://www.sitemaps.org/schemas/sitemap/0.9}url")
    SubElement(node, "{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text = url
    if modified:
        SubElement(node, "{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod").text = modified

ElementTree(urlset).write(ROOT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
print(f"Wrote {len(urls)} URLs to sitemap.xml")
