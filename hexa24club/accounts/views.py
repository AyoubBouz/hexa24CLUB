from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from accounts.forms import UserForm

def register(request):
    registered = False
    if request.method == 'POST':
        user_form =UserForm(data=request.POST)
        if user_form.is_valid():
            user =user_form.save()
            user.set_password(user.password)
            user.save()

            registered =True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        return render(request,'register.html',{'user_form':user_form})
