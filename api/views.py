from django.http import JsonResponse

def profile(request):
    data = {
        'name': 'Rui',
        'location': 'Portugal',
        'is_active': True,
        'age': 28
    }
    return JsonResponse(data)
