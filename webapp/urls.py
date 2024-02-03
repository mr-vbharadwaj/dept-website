from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.LoginView.as_view(),name='login'),
    path('studenthome/',views.StudentView.as_view(),name='studenthome'),
    path('facultyhome/',views.FacultyView.as_view(),name='facultyhome'),
    path('adminlogin/',views.AdminView.as_view(),name='adminlogin'),
    path('adminhome/',views.AdminHome.as_view(),name='adminhome'),
    path('adminhome/',views.DarkTheme.as_view(),name='adminhomedark'),
    path('adminhome/',views.LightTheme.as_view(),name='adminhomelight'),
    path('facultyresources/',views.FacultyResources.as_view(),name='facultyresources'),
    path('upload_resource/', views.upload_resource, name='upload_resource'),
    path('accounts/', include('django.contrib.auth.urls')),
]