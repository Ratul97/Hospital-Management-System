from tokenize import Special
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Doctor,Patient,Appointment


# Create your views here.
def home(request):
    return render(request,'Home.html')
def admin_login(request):
    error = ""
    if request.method == "POST":
            u = request.POST['uname']
            p = request.POST['pwd']
            user = authenticate(username=u,password=p)
            try:
                if user.is_staff:
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
    d={'error': error}
    return render(request,'login.html',d)

def signin(request):
    return render(request,'signin.html')
def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')
def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    d=0
    p=0
    a=0
    for i in doctor:
        d += 1
    for i in patient:
        p += 1
    for i in appointment:
        a += 1

    d1 = {'d' : d, 'p':p, 'a':a}
    return render(request, 'index.html' , d1)
    
def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('admin_login')

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request,'view_doctor.html',d)

def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['name']
        c = request.POST['mobile']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n,mobile=c,special=sp)
            error="no"
        except:
            error="yes"
    d={'error': error}
    return render(request,'add_doctor.html',d)

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()
    d = {'doc': doc}
    return render(request,'view_patient.html',d)

def delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
        try:
            Patient.objects.create(name=n,gender=g,mobile=m,address=a)
            error="no"
        except:
            error="yes"
    d={'error': error}
    return render(request,'add_patient.html',d)

def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == "POST":
        n = request.POST['doctor']
        p = request.POST['patient']
        da = request.POST['date']
        t = request.POST['time']

        doctor=Doctor.objects.filter(name=n).first()
        patient=Patient.objects.filter(name=p).first()

        try:
            Appointment.objects.create(
                doctor=doctor,patient=patient,date=da,time=t)
            error="no"
        except:
            error="yes"
    d={'doctor': doctor1, 'patient' : patient1, 'error': error}
    return render(request,'add_appointment.html',d)

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Appointment.objects.all()
    d = {'doc': doc}
    return render(request,'view_appointment.html',d)

def delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.get(id=pid)
    app.delete()
    return redirect('view_appointment')

