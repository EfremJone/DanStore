
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("account.urls") ),
    path('Admin/',include("Company_Admin.urls")),
    path('Store_Manager/',include("Store_manager.urls")),
]
