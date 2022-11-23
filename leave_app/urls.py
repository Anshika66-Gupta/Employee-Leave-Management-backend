from django.contrib import admin
from django.urls import path,include
from .views import LeaveApply,Search,ChangeStatus,FindLeave

urlpatterns = [
    
    path('applyleave',LeaveApply.as_view()),
    path('serach-leave',Search.as_view()),
    path('change-status',ChangeStatus.as_view()),
    path('findLeave/<str:id>',FindLeave.as_view()),
    
]