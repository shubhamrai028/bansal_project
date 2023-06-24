from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.getallschools, name ='getallschool'),
    path('getallstudent/<int:id>', views.getallstudents, name ='getallstudent'),
    path('create_school/', views.add_school, name ='add-school'),
    path('create_student/', views.add_student, name ='add-student'),
    path('deletestudent/<int:id>/<int:school_id>',views.deletestudent, name = 'deletestudent'),
    path('updatestudent/<int:id>',views.updatestudent, name = 'updatestudent'),
    path('update_student_save/<int:id>',views.update_student_save, name = 'update_student_save'),
    
    
    
    
    
   
]