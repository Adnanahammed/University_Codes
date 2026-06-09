import urllib.request
from bs4 import BeautifulSoup

url = "https://news.daum.net/ranking/popular"
html = urllib.request.urlopen(url)

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Extract page title
print("Page Title:", soup.title.get_text())

# Extract news headlines (assuming they are inside a tag/class like 'a.link_txt')
headlines = soup.select('a.link_txt')

for headline in headlines:
    print(headline.get_text())