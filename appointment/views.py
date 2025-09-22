from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
def home(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def services_view(request):
    return render(request, 'services.html')



from .models import Doctor

def dsignupaction(request):
    if request.method == 'GET':
        return render(request, 'dsignup.html')
    elif request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        phn = request.POST.get("phone")  # Ensure the form field name is 'phone'
        add = request.POST.get("address")  # Ensure the form field name is 'address'
        qua = request.POST.get("qualification")  # Ensure the form field name is 'qualification'

        if name and email and pwd and phn and add and qua:
            # Create a Doctor object and save it to the database
            doctor = Doctor(name=name, email=email, pwd=pwd, qualification=qua, phone=phn, address=add)
            doctor.save()
            
            return render(request, 'dsignup.html', {'msg': 'Please fill in all fields'})

        else:
            return render(request, 'dsignup.html', {'msg': 'Account created!'})

def dloginaction(request):
    if request.method == 'GET':
        return render(request, 'dlogin.html')
    elif request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        
        if name and email and pwd :
            # Create a Doctor object and save it to the database
            doctor = Doctor(name=name, email=email, pwd=pwd)
            doctor.save()
            
            return render(request, 'dlogin.html', {'msg': 'Please fill in all fields'})

        else:
            return render(request, 'dlogin.html', {'msg': 'Login Succesfull!'})




def dviewprofile(request):
    d=None
    if "demail" in request.session:
        e=request.session['demail']
        d=doctor.objects.filter(email__exact=e)
        return render(request, 'doctor.html',{'msg':'Session is expired, you can login !!'})
    else:
        return render(request, 'dviewprofile.html',{'data':d})

def dlogoutaction(request):
    
    if "demail" in request.session:
        del request.session['demail']
        return render(request, 'doctor.html')
    else:
        return render(request, 'dlogin.html',{'msg':'Session is expired,you can login!'})

def doctorhome(request):
    
    if "demail" in request.session:
        return render(request, 'index.html')
    else:
        return render(request, 'index.html',{'msg':'Session is expired,you can login!'})


from .models import Doctor

def psignupaction(request):
    if request.method == 'GET':
        return render(request, 'psignup.html')
    elif request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        phn = request.POST.get("phone")  # Ensure the form field name is 'phone'
        add = request.POST.get("address")  # Ensure the form field name is 'address'
        qua = request.POST.get("qualification")  # Ensure the form field name is 'qualification'

        if name and email and pwd and phn and add and qua:
            # Create a Doctor object and save it to the database
            doctor = Patient(name=name, email=email, pwd=pwd, qualification=qua, phone=phn, address=add)
            doctor.save()
            
            return render(request, 'psignup.html', {'msg': 'Please fill in all fields'})

        else:
            return render(request, 'psignup.html', {'msg': 'Account created!'})


def ploginaction(request):
    if request.method == 'GET':
        return render(request, 'plogin.html')
    elif request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        
        if name and email and pwd :
            # Create a Doctor object and save it to the database
            doctor = Patient(name=name, email=email, pwd=pwd)
            doctor.save()
            
            return render(request, 'plogin.html', {'msg': 'Please fill in all fields'})

        else:
            return render(request, 'plogin.html', {'msg': 'Login Succesfull!'})




def pviewprofile(request):
    d=None
    if "pemail" in request.session:
        e=request.session['pemail']
        d=patient.objects.filter(email__exact=e)
        return render(request, 'patient.html',{'msg':'Session is expired, you can login !!'})
    else:
        return render(request, 'pviewprofile.html',{'data':d})

def plogoutaction(request):
    
    if "pemail" in request.session:
        del request.session['pemail']
        return render(request, 'patient.html')
    else:
        return render(request, 'plogin.html',{'msg':'Session is expired,you can login!'})

def patienthome(request):
    
    if "pemail" in request.session:
        return render(request, 'index.html')
    else:
        return render(request, 'index.html',{'msg':'Session is expired,you can login!'})

