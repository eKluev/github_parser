import requests
from bs4 import BeautifulSoup
from lxml import html

# URL of your GitHub
url = "https://github.com/eKluev/"
repo = "?tab=repositories"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

resp = requests.get(url+repo, headers = headers)
soup = BeautifulSoup(resp.text, 'lxml')

for ul in soup.find_all('ul'):
	if ul.get('data-filterable-for') == "your-repos-filter":
		for link in ul.find_all('a'):
			link['href'] = "https://github.com" + link['href']
			link['target'] = "_blank"
		print(ul)
		break
