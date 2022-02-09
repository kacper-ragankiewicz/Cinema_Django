from django.urls import path, include
from .views import FilmLista, FilmDetale
from . import views


urlpatterns = [
    path('', FilmLista.as_view(), name='main_site'),
    path('film/<int:pk>/', FilmDetale.as_view(), name='detale'),
    path('login', views.login_site, name='login_site'),
    path('rejestracja', views.rejestracja, name='rejestracja'),
    # path('', views.logout, name='logout'),
]
