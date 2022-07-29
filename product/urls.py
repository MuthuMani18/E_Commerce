from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdectViewset

router = DefaultRouter()
router.register('product', ProdectViewset, basename='product')


urlpatterns = [

    path('', include(router.urls))
]
