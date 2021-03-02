from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User, auth
from . models import Data
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


class H(TemplateView):
    model = Data
    template_name = 'index.html'


class N(CreateView):
    model = Data
    template_name = 'new.html'
    fields = ['name', 'course', 'session', 'attendance', 'date', 'amount']
    success_url = reverse_lazy('home')


class R(ListView):
    model = Data
    template_name = 'records.html'


class U(UpdateView):
    model = Data
    fields = ['name', 'course', 'session', 'attendance', 'date', 'amount']
    template_name = 'edit.html'
    success_url = reverse_lazy('records')


class D(DeleteView):
    model = Data
    fields = ['name', 'course', 'session', 'attendance', 'date', 'amount']
    template_name = 'delete.html'
    success_url = reverse_lazy('records')


class CN(TemplateView):
    template_name = 'contact.html'


# def reg(request):
#     if request.method == 'POST':
#         username = request.POST['uname']
#         password = request.POST['pwd']
#         email = request.POST['mail']
#         user = User.objects.create_user(username=username, password=password, email=email)
#         user.save()
#         print("------Data are stored------")
#         return redirect('home')
#     else:
#         print("------NO DATA ENTERED------")
#         return render(request, 'login.html')


def student_login(request):
    if request.method == 'POST':
        uname = request.POST['un']
        pwd = request.POST['pd']
        user = auth.authenticate(username=uname, password=pwd)
        if user is not None:
            if user.is_superuser == 0:
                auth.login(request, user)
                print("----LOGIN SUCCESS|STUDENT----")
                return redirect('home')
            else:
                print("----NOT A STUDENT----")
                messages.info(request, "STUDENT LOGIN HERE")
                return redirect('login')
        else:
            print("----INVALID CREDENTIALS----")
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def out(request):
    auth.logout(request)
    return redirect('home')


def p(request):
    if request.method == 'POST':
        name = request.POST['un']
        pas = request.POST['pd']
        print(name, pas)


def admin_login(request):
    if request.method == 'POST':
        uname = request.POST['un']
        pwd = request.POST['pd']
        user = auth.authenticate(username=uname, password=pwd)
        if user is not None:
            if user.is_superuser == 1:
                auth.login(request, user)
                print("----LOGIN SUCCESS|ADMIN----")
                return redirect('records')
            else:
                print("----NOT AN ADMIN----")
                return redirect('records')
        else:
            print("----INVALID CREDENTIALS----")
            return redirect('records')
    else:
        return render(request, 'records.html')


def course(request):
    return render(request, 'courses.html')
