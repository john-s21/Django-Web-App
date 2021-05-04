from django.urls import path
from .import views as v


urlpatterns = [
    path('', v.H.as_view(), name='home'),
    # path('new_registration', v.N.as_view(), name='new'),
    path('records', v.R.as_view(), name='records'),
    path('update/<int:pk>', v.U.as_view(), name='edit'),
    path('delete/<int:pk>', v.D.as_view(), name='delete'),
    path('contact.html', v.CN.as_view(), name='contact'),
    path('login.html', v.student_login, name='login'),
    path('logout', v.out, name='logout'),
    path('admin_verify', v.admin_login, name='access'),
    path('course', v.course, name='course'),
    path('search', v.search_box, name='find'),
]
