from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('addnewcall', views.addnewcall, name='new-call'),
    path('calls-archive', views.callsarchive, name='calls-archive'),
    path('login', views.LoginView, name='login'),
    path('logout', views.LogoutView, name='logout'),
    path('calls/<int:pk>', views.CallDetailView.as_view(), name='call-detail')
]
