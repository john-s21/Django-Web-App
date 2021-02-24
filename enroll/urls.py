from django.urls import path
from .import views


urlpatterns = [
    path('', views.H.as_view(), name='home'),
    path('registration', views.N.as_view(), name='new'),
    path('records', views.R.as_view(), name='records'),
    path('update/<int:pk>', views.U.as_view(), name='edit'),
    path('delete/<int:pk>', views.D.as_view(), name='delete'),
    path('contact.html', views.CN.as_view(), name='contact'),
    path('login.html', views.log, name='login'),
    path('logout', views.out, name='logout'),
    path('admin_verify', views.log2, name='access'),
]
