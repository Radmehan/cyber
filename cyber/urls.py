
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('contact/',views.contact, name='contact'),
    path('schedule/',views.schedule, name='schedule'),
    
    path('reset_msg_id/', views.reset_msg_id, name='reset_msg_id'),
    path('logout/',views.logoutHandle ,name="logout"),
    
]
