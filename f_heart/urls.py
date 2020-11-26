from django.urls import path
from .views import index, register, about_us, our_programs

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("about_us/", about_us, name="about_us"),
    path("our_programs/", our_programs, name="our_programs" )    
]

