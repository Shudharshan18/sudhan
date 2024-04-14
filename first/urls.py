from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('logout/',views.logout_view,name="logout"),
    path('home/',views.home,name="home"),
    path('moviedetail/<int:id>/',views.moviedetail,name="moviedetail"),
    path('search/',views.search,name="search"),
]