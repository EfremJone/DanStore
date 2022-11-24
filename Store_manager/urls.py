from django.urls import path
from .import views
urlpatterns = [
   path('',views.store_dashboard,name="store-dashboard"),
   path('manage_catagory',views.manage_catagory,name="manage-catagory"),
   path('add_to_store',views.add_to_store,name="add-to-store"),
   path('cheek_request',views.cheeck_request,name="cheeck-request"),
]
