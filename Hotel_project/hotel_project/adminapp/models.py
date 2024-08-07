from django.db import models

# Create your models here.
class SliderImage(models.Model):
	slider_image=models.ImageField(upload_to = "static/uploads/")

class SliderText(models.Model):
	slider_heading=models.CharField(max_length=100)
	slider_content=models.TextField()
	slider_button_text=models.CharField(max_length=90)
	slider_button_link=models.TextField()


class HomeAboutUs(models.Model):
	about_us_heading=models.CharField(max_length=100)
	about_us_image1=models.ImageField(upload_to="static/uploads/")
	about_us_image2=models.ImageField(upload_to="static/uploads/")
	about_us_content=models.TextField()

class Rooms(models.Model):
	room_name=models.CharField(max_length=100)
	room_image=models.ImageField(upload_to="static/uploads/",null=True)
	room_pricing_per_day=models.IntegerField()
	room_size=models.CharField(max_length=100)
	room_capacity=models.CharField(max_length=100)
	room_features=models.TextField()
	room_details=models.TextField()


class Testimonials(models.Model):
	testimonials_name=models.CharField(max_length=100)
	start_testimnials=models.CharField(max_length=100)
	testimonials_details=models.TextField()
	img_testimnials=models.ImageField(upload_to="static/uploads/",null=True)


class Blog(models.Model):
	blog_name=models.CharField(max_length=100)
	blog_image=models.ImageField(upload_to="static/uploads/")
	blog_city=models.CharField(max_length=20)
	blog_info=models.CharField(max_length=100)
	blog_date=models.DateField()

class Services(models.Model):
	services_image=models.ImageField(upload_to="static/uploads/")
	services_details=models.CharField(max_length=100,null=True)
	services_name=models.TextField()

class About_Us(models.Model):
	about_heading=models.CharField(max_length=100)
	about_point1=models.CharField(max_length=100)
	about_point2=models.CharField(max_length=100)
	about_point3=models.CharField(max_length=100)
	about_point4=models.CharField(max_length=100)
	about_point5=models.CharField(max_length=100)
	about_content=models.TextField()

class About_Us_Image(models.Model):
	about_image=models.ImageField(upload_to="static/uploads/")
	about_title=models.CharField(max_length=100)

class Discovr(models.Model):
	background_image=models.ImageField(upload_to="static/uploads/")
	image_title=models.CharField(max_length=50)
	sub_title=models.CharField(max_length=100)
	video_link=models.TextField()


class Gallery(models.Model):
	gallery_image1=models.ImageField(upload_to="static/uploads/")
	gallery_image2=models.ImageField(upload_to="static/uploads/",null=True)
	gallery_image3=models.ImageField(upload_to="static/uploads/",null=True)
	gallery_image4=models.ImageField(upload_to="static/uploads/",null=True)