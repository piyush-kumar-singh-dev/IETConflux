from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject
# Create your views here.
def home(request):
    #return render(request,'files/home.html')
    a=Subject.objects.all()
    #ht=''
    #for i in a:
     #   ht+='<h1>'+i.Subjname+'</h1><br>'
    return render(request,'files/home.html',{'data':a})


