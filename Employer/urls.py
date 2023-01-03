from django.urls import path
from .import views
urlpatterns = [
   path('',views.employe_view,name="employe_dashboard"),
   path('emp_request',views.emp_request,name="emp_request"),
   path('emp_request2',views.emp_request2,name="emp_request2"),
   path('complet_request',views.complet_request,name="complet_request"),
   path('reste_request_form',views.reste_request_form,name="reste_request_form"),
  
    
]