import webbrowser
import re
from bs4 import BeautifulSoup
from urllib import request

plugin = input("Enter plugin-name: ")
url = f"https://plugins.trac.wordpress.org/browser/{plugin}/tags"

#response = request.urlopen(url)
#soup1 = BeautifulSoup(request.urlopen(url))\

response = request.urlopen(url)
soup1 = BeautifulSoup(response, "html.parser")

a_elements = soup1.find_all('a')
urls = [a['href'] for a in a_elements if a.has_attr('href')]

texts = [a.text for a in a_elements]

pattern = re.compile(r'^\d(\.\d)+$')


filtered_list = [s for s in texts if pattern.match(s)]

for i in filtered_list:
    print(i)
    webbrowser.open(f'https://plugins.trac.wordpress.org/browser/{plugin}/tags/{i}/README.txt')

