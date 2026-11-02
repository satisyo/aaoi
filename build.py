"""Rebuild index.html from template.html, page.html (the dashboard body) and data/*.json.
Usage: python3 build.py"""
import json, pathlib
root = pathlib.Path(__file__).parent
ids = ['snapshot', 'levels', 'scenarios', 'analysts', 'quarterly', 'factors', 'news']
data = {i: json.loads((root / 'data' / f'{i}.json').read_text()) for i in ids}
page = (root / 'page.html').read_text().replace('<meta name="dash-one-writer">', '')
tpl = (root / 'template.html').read_text()
out = tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False)).replace('__PAGE__', page)
(root / 'index.html').write_text(out)
print('built index.html', len(out))
