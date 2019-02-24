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
    d_list = []
    rank = 0

    # Loop over the identified top restaurants.
    for restaurant in restaurants:
        rank = rank + 1

        # Get restaurant name and rank.
        for restaurant_name in restaurant:
            restaurant_dict = {'name': restaurant_name, 'rank': rank, 'stars': None, 'address': None, 'country': None,
                               'directions': None, 'phone_no': None, 'email': None, 'website': None}

            # Scraping each of top restaurants specific web page.
            restaurant_url = base_url + restaurant.get('href')
            restaurant_html = simple_get(restaurant_url)

            # Generate bs object.
            restaurant_soup = BeautifulSoup(restaurant_html, 'html.parser')

            # Get country info.
            country = str(restaurant_soup.find('div', class_='address').p.get_text().strip()).split('\n')[2].strip()
            restaurant_dict['country'] = country

            # Get address info.
            address = str(restaurant_soup.find('div', class_='address').p.get_text().strip()).split('\n')[0].strip()
            restaurant_dict['address'] = address

            # Get star rating.
            star_rating = restaurant_soup.find('div', class_='star-rating').div
            content = star_rating['style']
            number = content.split(':')[1]
            only_number = number.split('%')[0]
            stars = round(((float(only_number) * 5)/100),2)
            restaurant_dict['stars'] = stars

            # Get phone_no.
            contacts_container = restaurant_soup.find('div', class_='contacts')
            for item in contacts_container.find_all('i', {"class": "fa fa-phone"}):
                phone_no = item.find_next_sibling("span").get_text()
                restaurant_dict['phone_no'] = phone_no

            # Get directions.
            for item in contacts_container.find_all('a', href=True):
                if "maps.google" in str(item):
                    direction = item['href']
                    restaurant_dict['directions'] = direction
                elif "mailto" in str(item):
                    email = item.text
                    restaurant_dict['email'] = email
                else:
                    website = item['href']
                    restaurant_dict['website'] = website

            d_list.append(restaurant_dict.copy())

    return d_list

if __name__ == '__main__':
    scrap_page()