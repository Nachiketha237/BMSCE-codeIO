from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.template import loader
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from .forms import CreateUserForm,CheckUserForm

# def register(request):
#   form=CreateUserForm()

#   template = loader.get_template('users/LOgin1.html')
#   return HttpResponse(template.render({ 'form':form},request))
    
def register(request):
    form=CreateUserForm()
    if request.method=='POST':
      form=CreateUserForm(request.POST)  
      if form.is_valid():
        form.save()
        messages.success(request, f'Your account has been created. You can log in now!')    
        return redirect('/users/Login')

    else:
     form=CreateUserForm()
    template = loader.get_template('users/Register.html')
    return HttpResponse(template.render({ 'form':form},request))

def login(request):
    if request.method=='POST':
      form=CheckUserForm(data=request.POST)
      if form.is_valid():
        return redirect('/users/')
    else:
      form=CheckUserForm()
    template = loader.get_template('users/Login.html')
    return HttpResponse(template.render({ 'form':form},request))
  

def users(request):
   return render (request,'user.html')



