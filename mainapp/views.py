from django.shortcuts import render
from rest_framework import serializers
from mainapp.serializers import SchoolSerilizer,StudentSerilizer
from rest_framework import status
from mainapp.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def add_school(request):
    school = SchoolSerilizer(data = request.data)
    if school.is_valid():
        school.save()
        resp = {'status':True,
                'message': 'School created successfully',
                'data': school.data}
        
        return Response(resp)
    
    
@api_view(['POST'])
def add_student(request):
    if Student.objects.filter(Enrollment = request.data['Enrollment']).exists():
        raise serializers.ValidationError('This Enrollment is alaready present')
    student = StudentSerilizer(data = request.data)
    if student.is_valid():
        student.save()
        resp = {'status':True,
                'message': 'Student created successfully',
                'data': student.data}
        return Response(resp)
    
    
    
@api_view(['GET'])
def getallstudents(request,id):
    students = Student.objects.filter(School = id)
    return render(request,"student_list.html",{'datalist':students})

@api_view(['GET'])
def getallschools(request):
    schools = School.objects.all()
    serializer = SchoolSerilizer(schools,many=True)
    return render(request,"school_list.html",{'datalist':serializer.data})
    
    
    
def deletestudent(request,id,school_id):
    students = Student.objects.get(Id = id)
    students.delete()
    student2 = Student.objects.filter(School = school_id)
    return render(request,"student_list.html",{'datalist': student2})


def updatestudent(request,id):
    students_exist_data = Student.objects.get(Id = id)
    schools = School.objects.all()
    return render(request,"student_update.html",{'students_exist_data':students_exist_data, 'schools':schools })


def update_student_save(request,id):
    students_exist_data = Student.objects.get(Id = id)
    school_id = request.POST.get('school_id')
    student_name = request.POST.get('student_name')
    school_obj = School.objects.get(Id =school_id )
    students_exist_data.School = school_obj
    students_exist_data.Name = student_name
    students_exist_data.save()
    schools = School.objects.all()
    serializer = SchoolSerilizer(schools,many=True)
    return render(request,"school_list.html",{'datalist':serializer.data})
    
    
    
    
    
    
    

