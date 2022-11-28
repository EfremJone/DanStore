from django.urls import path
from .import views
urlpatterns = [
   path('',views.store_dashboard,name="store-dashboard"),
    
   # -------- profile --------- #
   path('user_Profile',views.user_Profile,name="user-Profile"),
   path('edit_Profile',views.edit_Profile,name="edit-Profile"),
   path('chage_password',views.chage_password,name="chage_password"),
   path('chage_profile_pic',views.chage_profile_pic,name="chage-profile-pic"),
   path('delete_pic',views.delete_profile_pic,name="delete-pic"),
   # -------- End profile --------- #

   path('add_to_store',views.add_to_store,name="add-to-store"),
   path('cheek_request',views.cheeck_request,name="cheeck-request"),
   
   # ---------- Catagory ---------- #
   path('manage_catagory/',views.manage_catagory,name="manage-catagory"),
   path('add_new_catagory',views.add_new_catagory,name="new-catagory"),
   path('catagory_detail/<int:id>',views.catagory_detail,name="catagory-detail"),
   path('catagory_delete/<int:id>',views.delete_catagory,name="catagory-delete"),
   path('item_detail',views.item_detail,name="item-detail"),
   path('add_item/<int:id>',views.add_item,name="add-item"),

   # -------- End Catagory --------- #
]
