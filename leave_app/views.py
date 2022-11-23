
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employe, LeaveApplication
from rest_framework.response import Response
from employe_crud.serializer import EmployeSerializer,Leaveserializer
from django.db.models import Q
# Create your views here.
import json
# d8c0c0d2-cee9-4c79-a79a-4e0ebd5c35e0

class LeaveApply(APIView):
    permission_classes = []
    authentication_classes = []
    def post(self,request):
        data = request.data
        print(data)
        val = data['details']
        print(f'val= {val}')
        print()
        print()
        print(type(val))
        details = json.loads(val)
        print(type(details))
        # print(data['pdf'][0])
        file = request.FILES.get('pdf')
        if file:
            print('yes')
            print(file)
        print(details)
        try:

            employe = Employe.objects.get(employe_id = details['employe_id'])
            print(employe)
            if employe.total_leave > 3:
                return Response({'leave exceed 4'},status=400)
            leave = LeaveApplication.objects.create(leave_starting_date=details['starting_date'], leave_ending_date = details['ending_date'],Employe=employe,docfile=file)
            employe.total_leave = employe.total_leave + 1
            employe.save()
            return Response( {"leave applied"}, status=200)
        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc(e)
            return Response({'cheack the employee_id'}, status=400)



class Search(APIView):

    def post(self,request):
        data = request.data
        try:
            
            leave = LeaveApplication.objects.filter(Q(Employe__employe_name__icontains=data['key']) | Q(Employe__employe_id__icontains = data['key']) | Q (status__icontains =data['key']))
            leave_serializer = Leaveserializer(leave, many=True)
            return Response(leave_serializer.data,status=200)
        except Exception as e:
            print(e)
            return Response(status=400)


class ChangeStatus(APIView):

    def post(self, request):
        
        try:
            data = request.data
            leave = LeaveApplication.objects.get(id=data['id'])
            leave.status = data['status']
            leave.save()
            return Response({'leave applied succesfully'},status=200)
        except Exception as e:
            print(e)
            return Response(status=400)


class FindLeave(APIView):
    permission_classes = []
    authentication_classes = []
    def get(self,request,id):
        try:
            leave = LeaveApplication.objects.filter(Employe__employe_id = id)
            serializer = Leaveserializer(leave, many=True)
            return Response(serializer.data,status=200)
        except Exception as e:
            print(e)
            return Response(status=400)