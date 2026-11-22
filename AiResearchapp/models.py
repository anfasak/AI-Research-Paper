from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100, null =True, blank=True)
    usertype=models.CharField(max_length=100, null=True, blank=True)

class UsersTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    Gender=models.CharField(max_length=100,null=True,blank=True)

class CategoriesTable(models.Model):
    categoryName=models.CharField(max_length=100,null=True,blank=True)
    categoryDescription=models.CharField(max_length=100,null=True,blank=True)
    papercount=models.IntegerField(null=True,blank=True)    
    Image=models.FileField(upload_to='file/',null=True,blank=True)
    
class AnalyseReportsTable(models.Model):
        ReportTitle=models.CharField(max_length=100,null=True,blank=True)
        category=models.CharField(max_length=100,null=True,blank=True)
        date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
        

class FeedbackTable(models.Model):
        LOGINID= models.ForeignKey(UsersTable, on_delete=models.CASCADE, null=True, blank=True)
        date=models.DateField(auto_now_add=True ,null=True,blank=True)
        feedback=models.CharField(max_length=100,null=True,blank=True)
        Rating=models.IntegerField(null=True,blank=True)  
        
class UploadPapersTable(models.Model):
        LOGINID= models.ForeignKey(UsersTable, on_delete=models.CASCADE, null=True, blank=True)
        title=models.CharField(max_length=100,null=True, blank=True)
        categories=models.CharField(max_length=100, null=True, blank=True)
        description=models.CharField(max_length=100,null=True,blank=True)
        date=models.DateTimeField(auto_now_add=True,null=True, blank=True)            
        files=models.FileField(upload_to='image/',null=True,blank=True)
        
    
        
        