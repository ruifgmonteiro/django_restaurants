from api.handle_requests import simple_get
from bs4 import BeautifulSoup

def scrap_page():
	raw_html = simple_get('http://francesinhas.com/')
	soup = BeautifulSoup(raw_html, 'html.parser')

	# Get all text from div top-places.
	bodytext = soup.find(class_='top-places')
	restaurants = bodytext.find_all('a')
	for i in restaurants:
		for j in i:
			print(j)
	return j

if __name__ == '__main__':
	scrap_page()