from django.urls import path
from . import views
from .views import CreateUserView

urlpatterns = [
    path('search/<str:username>/', views.search_username, name='search_username'),
    path('api/search-user/', CreateUserView.as_view()),
]
