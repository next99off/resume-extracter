from django.db import models
from django.contrib.auth.models import User

class ResumeBasicInfoModel(models.Model):
    name = models.CharField(max_length= 200)
    email = models.EmailField()
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    postalcode=models.CharField(max_length=10)

class ResumeEducationInfoModel(models.Model):
    degree = models.CharField(max_length = 200)
    institution = models.CharField(max_length = 200)
    start = models.DateField()
    end = models.DateField()
    rank = models.CharField(max_length = 200)
    basic_info = models.ForeignKey(ResumeBasicInfoModel, on_delete= models.CASCADE, related_name="education_info") 

class ResumeExperienceInfoModel(models.Model):
    designation=models.CharField(max_length=50)
    exp_start=models.DateField()
    exp_end=models.DateField()
    company_name=models.CharField(max_length=100)
    company_rating=models.CharField(max_length=15)
    company_city=models.CharField(max_length=100)
    company_state=models.CharField(max_length=100)
    basic_info = models.ForeignKey(ResumeBasicInfoModel, on_delete= models.CASCADE, related_name="experience_info")

class LicenceInfoModel(models.Model):
    NPI_number = models.CharField(max_length=100) 
    basic_info = models.ForeignKey(ResumeBasicInfoModel, on_delete= models.CASCADE, related_name="license_info")

class AvailableStates(models.Model):
    state = models.CharField(max_length=100)
    basic_info = models.ForeignKey(ResumeBasicInfoModel, on_delete= models.CASCADE, related_name="available_states_info")

class ActiveInfoModel(models.Model):
    designation=models.CharField(max_length=50)
    active_start=models.DateField()
    company_name=models.CharField(max_length=100)
    company_rating=models.CharField(max_length=15)
    company_city=models.CharField(max_length=100)
    company_state=models.CharField(max_length=100)
    basic_info = models.ForeignKey(ResumeBasicInfoModel, on_delete= models.CASCADE, related_name="active_info")

class SpecialitiesModel(models.Model):
    speciality = models.CharField(max_length=100)
    years = models.IntegerField()
    basic_info = models.ForeignKey(ResumeBasicInfoModel, on_delete= models.CASCADE, related_name="speciality_info")
    