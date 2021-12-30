from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from .models import *


#Only class view
class Home_view(View):
    def get(self,request):
        return HttpResponse("I am Hemanta")

#Only template view
class template_view(TemplateView):
    template_name = "classApp/home.html"
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['name'] = "Hemanta"
        data['place'] = "Cuttack"
        data['DOB'] = 1999
        return data

#Only Listview using default template and Model

class default_list_view(ListView):
    model = PhoneModel

#Only listview using custom template and model

class custom_listView(ListView):
    model = PhoneModel
    template_name = "classApp/Phonedetails.html"
    context_object_name = 'PhoneList'

#Only listview using custom template and model
class details_view(DetailView):
    model = PhoneModel
    template_name = "classApp/PhoneData.html"
    context_object_name = 'Phones'
    
