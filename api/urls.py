from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('francesinhas/', views.get_francesinhas, name='francesinhas'),
]