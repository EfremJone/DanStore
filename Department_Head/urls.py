from django.urls import path
from .import views
urlpatterns = [
   path('',views.dept_head,name="dept-dashboard"),
   path('add_employe',views.add_employe,name="add_employe"),
   path('approve_request',views.approve_request,name="approve_request"),
   path('make_request',views.make_request,name="make_request"),
    
]