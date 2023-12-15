
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'booklist',views.BookAPIView)
router.register(r'authorlist',views.AuthorAPIView)

urlpatterns = [
    path('api/', include(router.urls)),
]
