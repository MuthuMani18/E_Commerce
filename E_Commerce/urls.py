from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("user.urls")),
    path("api/", include("My_Addresses.urls")),
    path("api/", include("product.urls")),
    path("api/", include("my_cart.urls")),
    path("api/", include("order.urls")),



]
