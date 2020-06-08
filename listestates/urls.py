from django.urls import path 
from .views import ListestatesView, ListestateView, SearchView

urlpatterns = [
    path('', ListestatesView.as_view()),
    path('search', SearchView.as_view()),
    path('<slug>', ListestateView.as_view()),
]