from django.urls import path
from . import views
from .models import Cocktail

app_name = 'barback'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('cocktail_form/', views.CreateView.as_view(model=Cocktail, success_url=('http://127.0.0.1:8000/barback/')), name='cocktail_form'),
    path('<int:cocktail_id>/save/', views.save, name='save'),
    path('<int:cocktail_id>/delete/', views.delete, name='delete'),
]
