from django.shortcuts import render,redirect
from crud.models import login
# Create your views here.
def create(request):
    context={}
    return render(request,'crud/create.html',context)

    
def store(request):
    myname=request.POST('name')
    mylast_mame=request.POST('last_name')
    myemail=request.POST('email')
    mycontact=request.POST('contact')

    login.objects.create(name=myname,last_name=mylast_mame,email=myemail,contact=mycontact)
    return redirect('/crud/create')

def read(request):
    result=login.objects.all()
    context={'result':result}
    return render(request,'crud/read.html',context)
