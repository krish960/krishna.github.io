from django.shortcuts import render
from adminapp import models
from django.http import HttpResponse
from website import models as usermodel
from django.shortcuts import redirect, render
# Create your views here.
def home(req):
	sliders = models.SliderImage.objects.all()
	slider_text = models.SliderText.objects.get(id=1)
	about=models.HomeAboutUs.objects.get(id=1)
	rooms=models.Rooms.objects.all()
	testimonialss=models.Testimonials.objects.all()
	blogs=models.Blog.objects.all()
	servicess=models.Services.objects.all()
	obj={"sliders":sliders,"slider_text":slider_text,"about":about,"rooms":rooms,"testimonialss":testimonialss,"blogs":blogs,"servicess":servicess}
	return render(req,"website/index.html",obj)

def rooms_us(req):
	return render(req,"website/rooms_us.html")


def about_us(req):
	saved_data=models.About_Us.objects.get(id=1)
	save_images=models.About_Us_Image.objects.all()
	discover_servicess=models.Discovr.objects.get()
	saved_gellery=models.Gallery.objects.get(id=1)
	obj={"saved_data":saved_data,"save_images":save_images,"discover_servicess":discover_servicess,"saved_gellery":saved_gellery}
	return render(req,"website/about_us.html",obj)


def blog(req):
	return render(req,"website/blog.html")

def contact(req):
	return render(req,"website/contact.html")

def save_contact(req):
	contact=usermodel.Contact(
		contact_name=req.POST['contact_name'],
		contact_email=req.POST['contact_email'],
		contact_message=req.POST['contact_message']
	)
	contact.save()
	return redirect("/contact")


def save_enquiry(req):
	# print(req.POST)
	enquiry=usermodel.Enquiry(
		check_in_date=req.POST['check_in_date'],
		check_out_date=req.POST['check_out_date'],
		guests=req.POST['guests'],
		room=req.POST['room'],
		user_name=req.POST['user_name'],
		mobile_number=req.POST['mobile_number']
	)
	enquiry.save()
	str="""
	<script>
		alert('Thanks For Enquiry');
		location.href="/";
	</script>
	"""
	return redirect("/")



	