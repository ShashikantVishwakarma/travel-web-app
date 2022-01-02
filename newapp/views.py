from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest=Destination.objects.all()
    return render(request,'index.html',{'dest':dest})

def news(request,id):
    data=Destination.objects.get(id=id)
    return render(request,'mumbai.html',{"data":data})

