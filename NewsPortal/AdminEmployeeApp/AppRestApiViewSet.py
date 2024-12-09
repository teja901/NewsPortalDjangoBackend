from .models import *
from AdminEmployeeApp.Appserializer import AdminEmployeSerializer
from django.http import JsonResponse
from rest_framework import generics,viewsets,status
from rest_framework.response import Response
from asgiref.sync import sync_to_async
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import action
import asyncio


async def async_task():
    await asyncio.sleep(2)  # Simulate a time-consuming async task
    return {"message": "Async task completed"}

class AdminEmployeviewset(viewsets.ModelViewSet):
    queryset=AdminEmployeeCredentials.objects.all()
    serializer_class=AdminEmployeSerializer
    
    @action(detail=True, methods=['get'],url_path='(?P<second>.+)/validateAdminAndEmloyee')
    async def validateAdminAndEmloyee(self,request,pk=None,second=None):
        user = await sync_to_async(
            lambda: AdminEmployeeCredentials.objects.filter(name=pk,password=second).values().first()
        )()

        if user:return Response(user, status=200)
        else:return Response(status=404)
        
    @action(detail=False, methods=['get'],url_path='validateAdminEmployee')
    def validateAdminEmployee(self, request):
     name = request.query_params.get('name')
     password = request.query_params.get('password')
     if not name or not password:
        return Response({'data': "Missing credentials"}, status=400)

     user = AdminEmployeeCredentials.objects.filter(name=name, password=password).values()
     if user:
        return Response({'data': list(user)}, status=200)
     else:
        return Response({'data': "Invalid user"}, status=404)
    
    @action(detail=False, methods=['post'])
    async def createAdmin(self,request):
        result = await async_task()  # Call async function
        return Response(result)
        
        # admin_employee = await sync_to_async(AdminEmployeeCredentials.objects.create)(
        #     name=request.data.get('username'),
        #     password=request.data.get('password')
        # )
        
        # Wait for the async operation to finish (forces it to run synchronously)
        # admin_employee = admin_employee.result()
        
        # serializer = self.get_serializer(admin_employee)
        
        # return Response({"data":}, status=201)
         

            