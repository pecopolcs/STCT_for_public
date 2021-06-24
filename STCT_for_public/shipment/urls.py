from django.urls import path
from .views import ShipmentList, ShipmentDetail

urlpatterns = [
    path('', ShipmentList.as_view()),
    path('shipmentlist/', ShipmentList.as_view()),
    path('shipmentdetail/<int:pk>/', ShipmentDetail.as_view()),
]