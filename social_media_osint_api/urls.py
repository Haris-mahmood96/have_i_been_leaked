from django.urls import path
from . import views
from .views import email_osint_analysis

urlpatterns = [
    path('search/<str:username>/', views.search_username, name='search_username'),
    path('osint/email/search/', email_osint_analysis, name='email_osint_analysis'),
]
