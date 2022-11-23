from rest_framework import serializers
from leave_app.models import LeaveApplication, Employe



class EmployeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employe
        fields = '__all__'



class Leaveserializer(serializers.ModelSerializer):
    Employe = EmployeSerializer(read_only = True)
    class Meta:
        model = LeaveApplication
        fields = "__all__"


       



