from django.db.models import fields
from rest_framework import serializers
from mainapp.models import Student,School

class SchoolSerilizer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        
        
class StudentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'