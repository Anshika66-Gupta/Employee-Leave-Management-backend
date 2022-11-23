from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    
    path('leave_details',views.LeaveReport.as_view()),
    path('employe-details',views.EmployeDetails.as_view()),
    path('employe-delete/<str:id>',views.DeleteEmploye.as_view()),

    path('create-employe',views.CreateEmploye.as_view()),
    path('get-single/<int:id>',views.GetSingleEmploye.as_view()),
    path('update/<str:id>',views.UpdateEmploye.as_view()),

    

]
