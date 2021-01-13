from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . models import Data, Reg
from django.urls import reverse_lazy
from django.shortcuts import render


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
        if request.POST.get('fname') and request.POST.get('lname'):
            post.f_name = request.POST.get('fname')
            post.l_name = request.POST.get('lname')
            post.usr_name = request.POST.get('uname')
            post.mail = request.POST.get('mail')
            post.save()
        return render(request, 'log.html')
    else:
        print("Please Enter valid details!!")
        return render(request, 'log.html')
