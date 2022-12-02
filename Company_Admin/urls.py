from django.urls import path
from .import views
urlpatterns = [
   path('',views.admin_dashboard,name="admin-dashboard"),
   path('add-user/',views.add_user,name="add-user")
   # -------- End profile --------- #


]
