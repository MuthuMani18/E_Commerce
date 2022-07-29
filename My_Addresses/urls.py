from django.db import router
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('address',views.AddressViewSet)

urlpatterns = [
    path('',include(router.urls))

]