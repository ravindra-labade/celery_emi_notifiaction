from django.urls import path
from .views import CustomerList, CustomerDetail




urlpatterns = [
    path('customers/', CustomerList.as_view() ),
    path('customers/<int:pk>/', CustomerDetail.as_view() ),
]
