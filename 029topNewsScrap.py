from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
#*.*.*/robots.txt

title = soup.find_all(name='a',class_='titlelink')
score = soup.select('.score')

titles = [t.text for t in title]
hrefs = [t.get('href') for t in title]
scores = [s.text.split(' ')[0] for s in score]
for t,s,h in zip(titles,scores,hrefs):
  print(s,'-->',t,'-->',h)