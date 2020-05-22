from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import sys

# https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def get_text(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

if __name__ == "__main__":
    url = sys.argv[1]
    html = urllib.request.urlopen(url).read()
    print(text_from_html(html))
