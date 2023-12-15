
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('api/booklist', views.BookAPIList.as_view(), name="list" ),
    path('api/booklist/<int:pk>/', views.BookAPIDetail.as_view(), name="num" ),

    path('api/authorlist', views.AuthorAPIList.as_view(), name="list" ),
    path('api/authorlist/<int:pk>/', views.AuthorAPIDetail.as_view(), name="num" ),

]
