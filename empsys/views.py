from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from empsys.models import Employee
from django import forms
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout




# Create your views here.

def employee_list(request):
    if request.method =="POST":
        emp_image = request.FILES.get('emp_image')  
        data = request.POST
        First_name = data.get('First_name')
        last_name =data.get('last_name')
        dob = data.get('dob')
        gender= data.get('gender')
        hire_date = data.get('hire_date')

        Employee.objects.create(First_name=First_name,
                                last_name=last_name,
                                dob=dob,
                                gender=gender,hire_date=hire_date,
                                emp_image=emp_image)
        return redirect('/')
    query_set = Employee.objects.all()
    context = {"employee_list":query_set}
   

    return render(request,'employee_list.html',context=context)



def delete_employee(request,id):
    Employee_data = Employee.objects.get(id=id)
    Employee_data.delete()
    return redirect('/')


def update_employe(request,id):
    update_employee_data = Employee.objects.get(id = id)
    if request.method =="POST":
        data = request.POST
        emp_image = request.FILES.get('emp_image')  
        First_name = data.get('First_name')
        last_name =data.get('last_name')
        dob = data.get('dob')
        gender= data.get('gender')
        hire_date = data.get('hire_date')

        update_employee_data.First_name= First_name
        update_employee_data.last_name= last_name
        update_employee_data.dob= dob
        update_employee_data.gender= gender
        update_employee_data.hire_date= hire_date

        if emp_image:
             update_employee_data.emp_image= emp_image

        update_employee_data.save()
        return redirect('/')


    data = {'update_employee_data':update_employee_data}
    return render(request,'update_employee.html',data )

def login_page(request):
    if request.method == "POST":
        try:
            if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                
                if not User.objects.filter(username = username).exists:
                     print('kkkkkkk')
                     messages.info(request, "username already exsit.please try another user name")
                     return redirect('/login/')
                user = authenticate(username = username, password = password)
                if user is None:
                    messages.info(request, "username and password is wrong")
                    return redirect('/login/')

                else:
                    login(request,user)
                    return redirect('/')
                
                    
            return redirect('/login/')
        except Exception as e:
            print(e)
    return render(request,'login.html')
    



def register_page(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email= request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.filter(username = username)
            print(user)
            
            if user.exists():

                messages.info(request, "username already exsit.please try another user name")
                return redirect('/register/')
                                
            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(password)
            new_user.save()

            messages.info(request, "account is created!!!")

            return redirect('/register/')
        return render(request,'register.html')
    except  Exception  as e:
        print(e)



def logout_page(request):
    logout(request)
    return redirect('/login/')