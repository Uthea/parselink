from bs4 import BeautifulSoup
import re

with open('file.html', 'br') as html:
    soup = BeautifulSoup(html, 'lxml')


match = soup.find('table', class_='showLinksTable')

for a in match.tbody.find_all('a'):
    link = a.get('href')
    math = re.compile(r'http://bc.vc/[0-9]+/(.+Shows.+.mkv)')
    if re.findall(math, link):
        print(re.findall(math, link)[0])
