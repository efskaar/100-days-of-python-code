from bs4 import BeautifulSoup
import requests

webpage = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(webpage.text,'html.parser')
movies = soup.select('img')
movie_titles = []
for movie in movies[1:-3]:
  title = movie.get('alt')
  if title.strip() != 'Amazon':
    movie_titles.append(title)

counter = 1
with open('030haveToWatch.txt','w') as outfile:
  for movie in movie_titles[::-1]:
    haveWatched = input(f'Have you watched {movie} Y/N:')
    if haveWatched.lower() != 'y':
      outfile.write(f'{counter},{movie}\n')
      counter += 1