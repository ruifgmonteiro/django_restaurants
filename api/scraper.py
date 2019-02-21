from api.handle_requests import simple_get
from bs4 import BeautifulSoup
from lxml import etree, html


# Scraping implementation. Should return a list of dictionaries.
def scrap_page():
	base_url = 'http://francesinhas.com'
	raw_html = simple_get(base_url)
	soup = BeautifulSoup(raw_html, 'html.parser')
	#print(soup)

	# Get all text from div top-places.
	top_places = soup.find(class_='top-places')
	restaurants = top_places.find_all('a')
	d = {}
	d_list = []
	position = 0
	for restaurant in restaurants:
		position = position + 1
		# Fetch do nome e posição do restaurante.
		for restaurant_name in restaurant:
			d['name'] = restaurant_name
			d['position'] = position
		#	print(j)
			restaurant_url = base_url + restaurant.get('href')
			restaurant_html = simple_get(restaurant_url)
			restaurant_soup = BeautifulSoup(restaurant_html, 'html.parser')
			addresses = restaurant_soup.find(class_='address')
			address = str(addresses.find_all('p'))
			new_soup = BeautifulSoup(address, 'html.parser')
			pretty_html = new_soup.prettify()
			pretty_string = str(pretty_html)
			print(pretty_string)
			d['address'] = pretty_string
			d_list.append(d.copy())
		#	print(d)

	return d_list

if __name__ == '__main__':
	scrap_page()