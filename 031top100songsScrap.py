from bs4 import BeautifulSoup
import requests

date = '2021-12-24'
webpage = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')

soup = BeautifulSoup(webpage.content,'html.parser')
row_elements = soup.find_all('div',class_='o-chart-results-list-row-container')

singers = [song.find('span',class_='a-no-trucate').text.strip('\n') for song in row_elements]
song_names = [song.find('h3',class_='c-title').text.strip('\n')for song in row_elements]
