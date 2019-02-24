from django.http import JsonResponse
from api.scraper import scrap_page

def get_francesinhas(request):
	data = scrap_page()
	return JsonResponse(data, safe=False)

if __name__ == '__main__':
	get_francesinhas()