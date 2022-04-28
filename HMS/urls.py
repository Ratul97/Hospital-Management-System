from django.contrib import admin
from django.urls import path
from HMS import views
import HMS


urlpatterns = [
    
     path('', views.home,name = "home"),
     path('Medicare/', views.home,name = "home"),
     path('Home/', views.home,name = "home"),
     path('admin_login/', views.admin_login,name = "admin_login"),
     path('signin/', views.signin,name = "signin"),
     path('aboutus/', views.aboutus,name = "aboutus"),
     path('contactus/', views.contactus,name = "contactus"),
     path('logout/',views.logout_admin,name="logout_admin"),
     path('index/',views.index,name="dashboard"),
     path('view_doctor/',views.view_doctor,name="view_doctor"),
     path('add_doctor/',views.add_doctor,name="add_doctor"),
     path('delete_doctor(?p<int:pid>)/',views.delete_doctor,name="delete_doctor"),
     path('view_patient/',views.view_patient,name="view_patient"),
     path('add_patient/',views.add_patient,name="add_patient"),
     path('delete_patient(?p<int:pid>)/',views.delete_patient,name="delete_patient"),
     path('view_appointment/',views.view_appointment,name="view_appointment"),
     path('add_appointment/',views.add_appointment,name="add_appointment"),
     path('delete_appointment(?p<int:pid>)/',views.delete_appointment,name="delete_appointment"),



]
