from django.urls import path
from . import views

urlpatterns = [
    path('search/<str:username>/', views.search_username, name='search_username'),
]
