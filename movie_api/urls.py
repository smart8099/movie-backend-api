# urls.py in your movies app
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieDataViewSet

router = DefaultRouter()
router.register(r'movies', MovieDataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
