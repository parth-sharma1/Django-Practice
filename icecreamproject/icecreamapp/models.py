from django.db import models


# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length = 100)
    email =  models.CharField(max_length = 100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    desc =  models.TextField()
    city = models.CharField(max_length=100)
    state_choices = [
        ("AP", "Andhra Pradesh"),
        ("AR", "Arunachal Pradesh"),
        ("AS", "Assam"),
        ("BR", "Bihar"),
        ("CT", "Chattisgarh"),
        ("GA", "Goa"),
        ("GJ", "Gujarat"),
        ("HR", "Haryana"),
        ("JH", "Jharkhand"),
        ("KA", "Karnataka"),
        ("KL", "Kerala"),
        ("UP", "Uttar Pradesh"), 
        ("UK", "Uttarakhand"),
        ("WB", "West Bengal")
    ]
    state=  models.CharField(max_length=10, choices=state_choices, default="UP")
    pincode = models.CharField(max_length=20)
    date = models.DateField()



    def __str__(self):
        return self.firstname
    