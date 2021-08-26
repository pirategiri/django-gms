from django.contrib import admin
from django.urls import path
from gyms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login/',views.login),
    path('register/',views.register),
    path('activate/',views.activate),
    path('profile/',views.profile),
    path('logout/',views.logout),
    path('profile/image',views.profile_image)
]
