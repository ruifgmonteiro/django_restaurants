from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    # ex: /api/francesinhas/
    path('profile/', views.profile, name='profile'),
]