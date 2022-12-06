from django.urls import path
from .import views

urlpatterns = [
    path('admin-dashboard', views.home, name='admin-dashboard'),
    path('manage-employee', views.manage_employee, name='manage-employee'),
    path('departments', views.departments, name='departments'),
    path('vendors', views.vendors, name='vendors'),
    path('role', views.role, name='role'),
    path('products', views.products, name='products'),
    path('store', views.store, name='store'),
    path('batch', views.batch, name='batch'),
    path('reports', views.reports, name='reports'),
    
    # 
    path('chat',views.chat,name="admin-chat"),
    path('chat_peple',views.chat_people,name="admin-chat_people"),
]