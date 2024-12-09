
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from AdminEmployeeApp.AppRestApiViewSet import AdminEmployeviewset
from .views import *
from ninja import NinjaAPI
from .app import router

api = NinjaAPI()

# api.add_router("/products/", router)

router=DefaultRouter()
router.register(r'AdminEmployeviewset',AdminEmployeviewset,basename='AdminEmployeviewset')
urlpatterns = [
   path('',include(router.urls)),
   #  path("api/", api.urls),
   path('demo',demo,name='demo'),
#    path('customer/get/', MyAsyncView.as_view({'get': 'getcustomer'}), name='get-customer'),
   path('customer/post/', my_async_view, name='post-customer'),
   path('async_task2',async_task2,name='async_task2'),
   path('dummyReq',dummyReq,name='dummyReq'),
   path('validateAdminEmployee/',validateAdminEmployee,name='validateAdminEmployee'),
]