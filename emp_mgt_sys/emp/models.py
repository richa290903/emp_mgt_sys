from django.db import models
class emp(models.Model):
      emp_photo=models.FileField(upload_to="emp/",max_length=250,null=True,default=None)
      first_name=models.CharField(max_length=15)
      last_name=models.CharField(max_length=15)
      dob=models.CharField(max_length=15)
      contact_no=models.CharField(max_length=11)
      email=models.CharField(max_length=20)
      address=models.CharField(max_length=200)

