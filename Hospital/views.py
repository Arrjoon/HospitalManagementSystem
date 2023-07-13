from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import Doctor, Patient, Appointmet

# Create your views here.


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def index(request):
    if not request.user.is_staff:
        return redirect("login")
    return render(request, 'index.html')


def login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_authenticated:
                auth_login(request, user)
                error = "no"
            else:
                error = 'yes'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, 'login.html', d)


def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('login')


def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {
        'doc': doc
    }
    return render(request, 'doctors.html', d)


def delete_doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def Add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['name']
        m = request.POST['mobile']
        s = request.POST['special']
        try:
            Doctor.objects.create(name=n, mobile=m, special=s)
            error = "no"
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, 'add_doctor.html', d)


def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.all()
    d = {'doc': patient}
    return render(request, 'patient.html', d)


def delete_patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
    try:
        p = Patient.objects.create(name=n, gender=g, mobile=m)
        p.save()
        error = "no"
    except:
        error = "yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)


def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == 'POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        dt = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointmet.objects.create(
                doctor=doctor, patient=patient, date=dt, time=t)
            error = "no"
        except:
            error = "yes"
    d = {'patient': patient1,
         'doctor': doctor1,
         'error': error}
    return render(request, 'add_appointment.html', d)


def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointmet.objects.all()
    d = {'doc': appointment}

    return render(request, 'view_appointment.html', d)
