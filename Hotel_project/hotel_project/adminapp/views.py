from django.shortcuts import render
from adminapp import models
from django.http import HttpResponse
from django.shortcuts import redirect, render
from website import models as usermodel
# Create your views here.

def home(req):
	enquiry=usermodel.Enquiry.objects.all()
	obj={"enquiry":enquiry}
	return render(req,"adminapp/index.html",obj)
def slider(req):
	sliders=models.SliderImage.objects.all()
	obj={"sliders":sliders}
	return render(req,"adminapp/slider.html",obj)

def save_slider_image(req):
	# return render(req,"adminapp/save_slider.html")
	slider=models.SliderImage(
		slider_image=req.FILES['slider_image']
	)
	slider.save()
	# return HttpResponse("data")
	return redirect("/admin/slider")

def delted_slidet(req):
	order_id=req.GET['id']
	models.SliderImage.objects.get(id = order_id).delete()
	return redirect("/admin/slider")


def slider_text(req):
	text = models.SliderText.objects.get(id=1)
	obj={"text":text}
	return render(req,"adminapp/slider_text.html",obj)

def save_slider_text(req):
	# text = models.SliderText(
	# 	slider_heading=req.POST['slider_heading'],
	# 	slider_content=req.POST['slider_content'],
	# 	slider_button_text=req.POST['slider_button_text'],
	# 	slider_button_link=req.POST['slider_button_link']
	# )
	# text.save()
	text = models.SliderText.objects.get(id=1)
	text.slider_heading =req.POST['slider_heading']
	text.slider_content=req.POST['slider_content']
	text.slider_button_text=req.POST['slider_button_text']
	text.slider_button_link=req.POST['slider_button_link']
	text.save()
	return redirect("/admin/slider_text")


def home_about(req):
	about=models.HomeAboutUs.objects.get(id=1)
	obj={"about":about}
	return render(req,"adminapp/home_about.html",obj)

def save_home_about(req):
	about=models.HomeAboutUs.objects.get(id=1)
	about.about_us_heading=req.POST['about_us_heading']
	if "about_us_image1" in req.FILES:
		about.about_us_image1=req.FILES['about_us_image1']
	if "about_us_image2" in req.FILES:
		about.about_us_image2=req.FILES['about_us_image2']
	about.about_us_content=req.POST['about_us_content']
	about.save()
	return redirect("/admin/home_about")


def add_room(req):
	return render(req,"adminapp/add_room.html")

def save_room(req):
	room = models.Rooms(
		room_name=req.POST['room_name'],
		room_image=req.FILES['room_image'],
		room_pricing_per_day=req.POST['room_pricing_per_day'],
		room_size=req.POST['room_size'],
		room_capacity=req.POST['room_capacity'],
		room_features=req.POST['room_features'],
		room_details=req.POST['room_details'],
	)
	room.save()
	return redirect("/admin/add_room/")

def room_list(req):
	rooms=models.Rooms.objects.all()
	obj={"rooms":rooms}
	return render(req,"adminapp/room_list.html",obj)

def testimonials(req):
	return render(req,"adminapp/testimonials.html")

def save_testimonials(req):
	testi = models.Testimonials(
		testimonials_name=req.POST['testimonials_name'],
		start_testimnials=req.POST['start_testimnials'],
		testimonials_details=req.POST['testimonials_details'],
		img_testimnials=req.FILES['img_testimnials'],
	)
	testi.save()
	return redirect("/admin/testimonials")

def testimonials_list(req):
	testimonialss=models.Testimonials.objects.all()
	obj={"testimonialss":testimonialss}
	return render(req,"adminapp/testimonialss.html",obj)


def add_blog(req):
	return render(req,"adminapp/add_blog.html")

def save_blog(req):
	blog=models.Blog(
		blog_name=req.POST['blog_name'],
		blog_image=req.FILES['blog_image'],
		blog_city=req.POST['blog_city'],
		blog_info=req.POST['blog_info'],
		blog_date=req.POST['blog_date'],
	)
	blog.save()
	return redirect("/admin/add_blog")

def blog_list(req):
	blogs=models.Blog.objects.all()
	obj={"blogs":blogs}
	return render(req,"adminapp/blog_list.html",obj)

def Add_services(req):
	return render(req,"adminapp/Add_services.html")

def save_services(req):
	services=models.Services(
		services_image=req.FILES['services_image'],
		services_name=req.POST['services_name'],
		services_details=req.POST['services_details'],
	)
	services.save()
	return redirect("/admin/Add_services")

def services_list(req):
	servicess=models.Services.objects.all()
	obj={"servicess":servicess}
	return render(req,"adminapp/services_list.html",obj)

def rooms_us(req):
	return render(req,"adminapp/about_us.html")

def Add_about(req):
	saved_data=models.About_Us.objects.get(id=1)
	obj={"saved_data":saved_data}
	return render(req,"adminapp/Add_about.html",obj)

def save_about_us_new(req):
	saved_data=models.About_Us.objects.get(id=1)
	saved_data.about_heading=req.POST['about_heading']
	saved_data.about_point1=req.POST['about_point1']
	saved_data.about_point2=req.POST['about_point2']
	saved_data.about_point3=req.POST['about_point3']
	saved_data.about_point4=req.POST['about_point4']
	saved_data.about_point5=req.POST['about_point5']
	saved_data.about_content=req.POST['about_content']
	saved_data.save()
	return redirect("/admin/Add_about")

def add_about_us_images(req):
	save_images=models.About_Us_Image.objects.all()
	obj={"save_images":save_images}
	return render(req,"adminapp/add_about_us_images.html",obj)

def save_about_image(req):
	save_image=models.About_Us_Image(
		about_image=req.FILES['about_image'],
		about_title=req.POST['about_title'],
	)
	save_image.save()
	return redirect("/admin/add_about_us_images")

def add_about_discover_service(req):
	discover_servicess=models.Discovr.objects.get()
	obj={"discover_servicess":discover_servicess}
	return render(req,"adminapp/add_about_discover_service.html",obj)

def save_discover_services(req):
	discover_servicess=models.Discovr.objects.get()
	discover_servicess.background_image=req.FILES['background_image']
	discover_servicess.image_title=req.POST['image_title']
	discover_servicess.sub_title=req.POST['sub_title']
	discover_servicess.video_link=req.POST['video_link']
	discover_services.save()
	return redirect("/admin/add_about_discover_service")

def delet_bookin_detles(req):
	order_id=req.GET['id']
	usermodel.Enquiry.objects.get(id = order_id).delete()
	return redirect("/")

def add_gallery(req):
	saved_gellery=models.Gallery.objects.get(id=1)
	obj={"saved_gellery":saved_gellery}
	return render(req,"adminapp/add_gallery.html",obj)

def save_gallery(req):
	saved_gellery=models.Gallery.objects.get(id=1)
	saved_gellery.gallery_image1=req.FILES['gallery_image1']
	saved_gellery.gallery_image2=req.FILES['gallery_image2']
	saved_gellery.gallery_image3=req.FILES['gallery_image3']
	saved_gellery.gallery_image4=req.FILES['gallery_image4']
	saved_gellery.save()
	return redirect("/admin/add_gallery")

def content(req):
	contact=usermodel.Contact.objects.all()
	obj={"contact":contact}
	return render(req,"adminapp/content.html",obj)

