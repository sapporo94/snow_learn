from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[1]
missing=[]
for f in root.rglob('*.html'):
    soup=BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
    for a in soup.find_all(['a','link','script']):
        href=a.get('href') or a.get('src')
        if not href or href.startswith(('http://','https://','mailto:','#')): continue
        path=href.split('#')[0]
        if not path: continue
        target=(f.parent/path).resolve()
        if not target.exists(): missing.append((str(f.relative_to(root)), href))
print(f'HTML files: {len(list(root.rglob("*.html")))}')
print(f'Missing local links: {len(missing)}')
for m in missing: print(m)
raise SystemExit(1 if missing else 0)
