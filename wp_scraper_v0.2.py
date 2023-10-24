import webbrowser
import re
import requests
from bs4 import BeautifulSoup
from urllib import request

def list_url(sorted_url):

    urls = []

    for a in sorted_url:
        if a.has_attr('href'):
            urls.append(a['href'])

    return urls

def main():
  
  plugin = input("Podaj nazwę wtyczki: ")
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0'}

  url = f"https://plugins.trac.wordpress.org/browser/{plugin}/tags"

  response = request.urlopen(url)
  soup = BeautifulSoup(response, "html.parser")
  sorted_url = soup.find_all('a')
  urls = list_url(sorted_url)

  texts = [a.text for a in sorted_url]
  pattern = re.compile(r'^\d(\.\d)+$')
  filtered_list = [s for s in texts if pattern.match(s)]

  print('Filtered list: ', filtered_list)

  for i in filtered_list:
    print(i)

  for i in filtered_list:

    check = requests.get(f'https://plugins.trac.wordpress.org/browser/{plugin}/tags/{i}/README.txt', headers=headers)

    if check.status_code == 404:
       print('pierwszy if')
       webbrowser.open(f'https://plugins.trac.wordpress.org/browser/{plugin}/tags/{i}/readme.txt')
    else:
       print('drugi if')
       webbrowser.open(f'https://plugins.trac.wordpress.org/browser/{plugin}/tags/{i}/README.txt')



if __name__ == "__main__":
  main()
