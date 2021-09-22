import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://dead-programmer.com/free-course/"
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
links = soup.find_all('h3',{'class':'elementor-post__title'})
links = [link.find('a').get('href') for link in links]
links = list(set(links))

udemy_links = list()
for link in links :
	r = requests.get(link)
	soup = BeautifulSoup(r.text,'html.parser')
	btn = soup.find('a',{'class':'su-button su-button-style-stroked'})
	udemy_links.append(btn.get('href'))

data = {
	'url':udemy_links
}
df = pd.DataFrame(data)
df.to_csv('courses.csv')
