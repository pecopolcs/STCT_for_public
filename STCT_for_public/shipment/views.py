from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import InfoModel

class ShipmentList(ListView):
    template_name = 'shipmentlist.html'
    model = InfoModel

class ShipmentDetail(DetailView):
    template_name = 'shipmentdetail.html'
    model = InfoModel