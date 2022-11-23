from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from leave_app.models import LeaveApplication, Employe
from .serializer import Leaveserializer, EmployeSerializer

class LeaveReport(APIView):
    
    def get(self, request):
        try:
            leave_details = LeaveApplication.objects.all().order_by('-id')
            
            leave_serializer = Leaveserializer(leave_details,many=True)
            return Response(leave_serializer.data,status=200)
        except Exception as e:
            print(e)
            return Response(status=200)

class EmployeDetails(APIView):
    
    def get(self, request):
        try:
            employe_list = Employe.objects.all()
            employe_serializer = EmployeSerializer(employe_list, many=True)
            return Response(employe_serializer.data, status=200)
        except:
            return Response(status=400)


class DeleteEmploye(APIView):
    
    def delete(self, request, id):
        try:
            print('waiting')
            Employe.objects.get(employe_id=id).delete()
            print('nice')
            return Response({'employee deleted'},status=200)
        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc(e)
            return Response(status=400)

class CreateEmploye(APIView):
    
    def post(self, request):
        try:
            data = request.data
            employe = Employe.objects.create(**data)
            return Response({'employe created'},status=200)
        except:
            return Response({'failed'},status=400)
class GetSingleEmploye(APIView):

    def get(self, request,id):
        employe = Employe.objects.get(id=id)
        serializer = EmployeSerializer(employe)
        return Response(serializer.data, status=200)

class UpdateEmploye(APIView):

    def post(self,request,id):
        data = request.data
        print(data)
        employe = Employe.objects.filter(id=id)
        employe.update(**data)
        
        return Response({'updated'},status=200)