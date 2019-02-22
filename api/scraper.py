from api.handle_requests import simple_get
from bs4 import BeautifulSoup

# Scraping implementation. Should return a list of dictionaries.
def scrap_page():
	# Scraping base url.
	base_url = 'http://francesinhas.com'
	raw_html = simple_get(base_url)
	soup = BeautifulSoup(raw_html, 'html.parser')

	# Isolate target code.
	top_places = soup.find(class_='top-places')
	restaurants = top_places.find_all('a')

	# Initialize dict, list of dicts (will be used as response) and rank.
	d = {}
	d_list = []
	rank = 0

	# Loop over the detected top restaurants.
	for restaurant in restaurants:
		rank = rank + 1
		# Get restaurant name and rank.
		for restaurant_name in restaurant:
			d['name'] = restaurant_name
			d['rank'] = rank

			# Scraping each of top restaurants specific web page.
			restaurant_url = base_url + restaurant.get('href')
			restaurant_html = simple_get(restaurant_url)

			# Generate bs object.
			restaurant_soup = BeautifulSoup(restaurant_html, 'html.parser')

			# Find all p's.
			address = restaurant_soup.find('div', class_='address').p

			sep = '<br'
			rest = str(address).split(sep, 1)[0]
			new_sep = '<p>'
			new_rest = rest.split(new_sep, 1)[1]
			final = new_rest.strip()

			d['address'] = final

			d_list.append(d.copy())

	return d_list

if __name__ == '__main__':
	scrap_page()