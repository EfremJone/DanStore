from django.urls import path
from .import views
urlpatterns = [
   path('',views.store_dashboard,name="store-dashboard"),
   path('manage_catagory',views.manage_catagory,name="manage-catagory"),
   path('add_to_store',views.add_to_store,name="add-to-store"),
   path('cheek_request',views.cheeck_request,name="cheeck-request"),
   # -------- profile --------- #
   path('user_Profile',views.user_Profile,name="user-Profile"),
   path('edit_Profile',views.edit_Profile,name="edit-Profile"),
   path('chage_password',views.chage_password,name="chage_password"),
   path('chage_profile_pic',views.chage_profile_pic,name="chage-profile-pic"),
   # -------- End profile --------- #


]
