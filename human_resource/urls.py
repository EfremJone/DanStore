from django.urls import path
from .import views
urlpatterns = [
   path('',views.hr_dashboard,name="hr_dashboard"),
    # MANAGE EMPLOYEE
    path('hr_manage-employee', views.manage_employee, name='hr-manage-employee'),
    path('hr_add-new-employe',views.add_new_employe, name='hr-add-new-employe'),
    path('employe-ditel/<int:id>',views.employe_ditel, name='employe-ditel'),
    path('aprove-employe',views.aprove_employe, name='hr-aprove-employe'),
    path('unaproveEmploye-ditel/<int:id>',views.unapproveEmploye_ditel, name='un-employe-ditel'),
    path('rejected_emp_approved_request',views.rejected_emp_approved_request, name='rejected-emp-approved-request'),
    path('reject-request-unemp/<int:id>',views.reject_request, name='reject-request-unemp'),
     
   
    path('approve-unaproved-emp/<int:id>',views.approve_unaproved_emp, name='approve-unaproved-emp'),
    
    #  End Employe 
     
    # MANAGE DEPARTMENT
    path('hr_department', views.hr_department, name='hr-department'),
    path('hr_department_detail/<int:id>', views.hr_department_detail, name='hr-department-detail'),
    path('hr_add-new-department',views.hr_add_new_department,name='hr_add-new-department'),
    path('add_emp_to_dep', views.add_emp_to_dep, name='add_emp_to_dep'),
    
    # END DEPARTMENT  
   ]