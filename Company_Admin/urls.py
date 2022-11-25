from django.urls import path
from .import views
urlpatterns = [
   path('',views.store_dashboard,name="admin-dashboard"),
   
   # -------- End profile --------- #


]
