from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
"""from django.contrib.auth.models import auth"""
from . models import Data, Reg
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


class H(TemplateView):
    model = Data
    template_name = 'home.html'


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


def log(request):
    if request.method == 'POST':
        post = Reg()
        post.usr_name = request.POST.get('uname')
        post.pwd = request.POST.get('pwd')
        post.mail = request.POST.get('mail')
        post.save()
        print("------Data are stored------")
        return redirect('home')
    else:
        print("------NO DATA ENTERED------")
        return render(request, 'log.html')


"""def reg(request):
    if request.method == 'POST':
        post = Reg()
        post.usr_name = request.POST.get('uname')
        post.pwd = request.POST.get('pwd')
        if auth.authenticate(usr_name='uname', pwd='pwd'):
            pass
    else:
        pass"""
