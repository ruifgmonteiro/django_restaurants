from django.http import JsonResponse
from api.scraper import scrap_page

def get_francesinhas(request):
	'''
	data = [
	{'name': 'Café Santiago',
	 'position': 1,
	 'stars': 4,
	 'address': 'R. de Passos Manuel 226, 4000 Porto ',
	 'country': 'Portugal',
	 'coordinates': '41.146553,-8.604884',
	 'phone_no': 222055797,
	 'email': None,
	 'website': None},
	{'position': 2,
	'name': 'Tappas Caffé',
	'stars': 4,
	'address': 'Rua Doutor António Granjo 549, 4400 Vila Nova de Gaia ',
	'country': 'Portugal',
	'coordinates': 'link',
	'phone_no': 223706196,
	'email': 'tappascaffe@gmail.com',
	'website': 'http://www.tappascaffe.com/'}
	]

	return JsonResponse(data, safe=False)
	'''
	data = scrap_page()
	return JsonResponse(data, safe=False)

if __name__ == '__main__':
	get_francesinhas()