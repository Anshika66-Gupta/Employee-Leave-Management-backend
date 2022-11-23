from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from leave_app.models import Employe, LeaveApplication
from .models import Accounts
from employe_e import settings
import jwt
from django.http.response import JsonResponse
# Create your views here.
# class LeaveApply(APIView):

#     def post(self,request):
#         data = request.data
#         try:
#             employe = Employe.objects.get(employe_id = data['employe_id'])
#             leave = LeaveApplication.objects.create(leave_starting_date=data['starting_date'], leave_ending_date = data['ending_date'])
#             return Response( {"leave applied"}, status=200)
#         except:
#             return Response({'cheack the employee_id'}, status=400)


# def jack(request):
#     return HttpResponse("hello")

class Verifyss(APIView):
    permission_classes = []
    authentication_classes = []
    
    def post(self,request,*args,**kwargs):
        data = request.data
        token = data['token']
        
        tokens = str(token)
        try:
            user_jwt = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print(user_jwt['user_id'])
            user = Accounts.objects.get(id=user_jwt['user_id'])
            val = {'username':user.username, 'status':'true'}
            return JsonResponse(val,safe=False)
        except Exception as e:
            val = {'status':'false'}
            return JsonResponse(val,safe=False)