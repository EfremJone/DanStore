from django.urls import path
from .import views
urlpatterns = [
   path('',views.dept_head,name="dept-ashboard"),
    
]