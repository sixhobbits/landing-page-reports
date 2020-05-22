from url_to_html import get_html
from html_to_text import get_text

import dbhelper as db

import sys

name = sys.argv[1]
url = sys.argv[2]

html = get_html(url)
text = get_text(html)

db.add_page(name, url, html, text)
print("added", name)

