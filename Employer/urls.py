from django.urls import path
from .import views
urlpatterns = [
   path('',views.employe_view,name="employe_dashboard"),
   path('request',views.request,name="request"),
  
    
]