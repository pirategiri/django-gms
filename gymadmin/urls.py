from django.contrib import admin
from gymadmin import views
from django.urls import path
urlpatterns = [
  path('admin/', admin.site.urls),
  path('dashboard/',views.dashboard),
  path('gyms/CreateGym/',views.CreateGym),
  path('gyms/',views.gyms),
  path('gyms/details/<int:gym_id>',views.details),
  path('gyms/delete/<int:gym_id>',views.delete),
  path('gyms/edit/<int:gym_id>',views.edit),
 

]