import asyncio
from django.http import HttpResponse
from django.shortcuts import render
from asgiref.sync import sync_to_async
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.http import JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from django.views.decorators.http import require_http_methods
import requests
from rest_framework.decorators import api_view


def demo(request):
    # Use sync_to_async directly on the ORM call
    # result = await sync_to_async(lambda: AdminEmployeeCredentials.objects.create(
    #         name="Teja",
    #         password="12345"
            
    #     ))()
    return HttpResponse("Hi Demo")
        

    # Return the result as a response
    return HttpResponse(str(result))  # Convert the result to string for response

def dummyReq(request):
    res=requests.get('https://0ed6-2409-40f0-103a-666d-9481-8736-2654-fbf2.ngrok-free.app/AdminEmployee/validateAdminEmployee/Teja/12345')
    print(res.json())
    return HttpResponse("Hi working")

async def create(request):
    sync_to_async(lambda : AdminEmployeeCredentials.objects.create())
    
    

@sync_to_async
def get_all_customers():
    return list(AdminEmployeeCredentials.objects.all())

# Define your async view
class MyAsyncView(APIView):
    async def getcustomer(self):
        customers = await get_all_customers()  # Fetch customers asynchronously
        return Response({"customers": customers})
    


async def async_task():
    print("Task1")
    await asyncio.sleep(3)  # Simulate a time-consuming task
    return {"status": "success", "message": "Async task completed"}

async def async_task2(request):
    print("Task2")
    await asyncio.sleep(1)  # Simulate a time-consuming task
    return JsonResponse({"status": "success12345ppp"})
# @api_view(['POST'])
# async def my_async_view(request):
#     # Call an asynchronous task
#     result = await async_task()
#     return Response(result)
import json
from django.views.decorators.csrf import csrf_exempt
@require_http_methods(["POST"])
@csrf_exempt
async def my_async_view(request):
    print(json.loads(request.body))
    # await sync_to_async(lambda : AdminEmployeeCredentials.objects.create(name="Teja",
    #         password="12345"
            
    #     ))()
    data=await sync_to_async(lambda : list(AdminEmployeeCredentials.objects.values()))()
    print(data)
    await asyncio.gather(async_task2(),async_task())
    # result = await async_task()

    return JsonResponse({"message": data })

@sync_to_async
def db_data(username, password):
    return list(AdminEmployeeCredentials.objects.all().values())

# Async view for validateAdminEmployee
@api_view(['GET'])
async def validateAdminEmployee(request):
    try:
        # Await the db_data function for asynchronous DB access
        user = await db_data("TEJA", "123")
        print(user)
        if user:
            return Response({"data": "Success"}, status=200)
        else:
            return Response({"data": "Invalid user"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
