"""
URL configuration for hotel_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website import views as user
from adminapp import views as adminas

urlpatterns = [
    path('',user.home),
    path('rooms_us/',user.rooms_us),
    path('about_us/',user.about_us),
    path('blog/',user.blog),
    path('contact/',user.contact),
    path('save_enquiry/',user.save_enquiry),
    path('save_contact/',user.save_contact),

    path('admin/',adminas.home),
    path('admin/content/',adminas.content),
    path('admin/slider',adminas.slider),
    path('admin/save_slider_image/',adminas.save_slider_image),
    path('admin/delted_slidet',adminas.delted_slidet),
    path('admin/slider_text/',adminas.slider_text),
    path('admin/save_slider_text/',adminas.save_slider_text),
    path('admin/home_about/',adminas.home_about),
    path('admin/save_home_about/',adminas.save_home_about),
    path('admin/add_room/',adminas.add_room),
    path('admin/save_room/',adminas.save_room),
    path('admin/room_list/',adminas.room_list),
    path('admin/testimonials/',adminas.testimonials),
    path('admin/save_testimonials/',adminas.save_testimonials),
    path('admin/testimonials_list/',adminas.testimonials_list),
    path('admin/add_blog/',adminas.add_blog),
    path('admin/save_blog/',adminas.save_blog),
    path('admin/blog_list/',adminas.blog_list),
    path('admin/Add_services/',adminas.Add_services),
    path('admin/save_services/',adminas.save_services),
    path('admin/services_list/',adminas.services_list),
    # about us
    path('admin/',adminas.rooms_us),
    # path('admin/Add_about_new_point/',adminas.Add_about_new_point),
    # path('admin/save_about_us/',adminas.save_about_us),
    path('admin/Add_about/',adminas.Add_about),
    path('admin/save_about_us_new/',adminas.save_about_us_new),
    path('admin/add_about_us_images/',adminas.add_about_us_images),
    path('admin/save_about_image/',adminas.save_about_image),
    path('admin/add_about_discover_service/',adminas.add_about_discover_service),
    path('admin/save_discover_services/',adminas.save_discover_services),
    path('admin/delet_bookin_detles/',adminas.delet_bookin_detles),
    # path('admin/add_gallery/',adminas.add_gallery),
    path('admin/add_gallery/',adminas.add_gallery),
    path('admin/save_gallery/',adminas.save_gallery),
    
]
