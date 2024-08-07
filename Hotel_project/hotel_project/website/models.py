from django.db import models

# Create your models here.
class Enquiry(models.Model):
	check_in_date=models.CharField(max_length=40)
	check_out_date=models.CharField(max_length=40)
	guests=models.IntegerField()
	room=models.CharField(max_length=100)
	user_name=models.CharField(max_length=100,null=True)
	mobile_number=models.CharField(max_length=100,null=True)

class Contact(models.Model):
	contact_name=models.CharField(max_length=100)
	contact_email=models.CharField(max_length=100)
	contact_message=models.TextField()
