from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .forms import *

from .models import *

# Create your views here.


# ======================Administraion=====================

class LoginView(View):
    def get(self,request):
        return render(request,'Administration/Admin_login.html')
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            obj = LoginTable.objects.get(username=username,password=password)
            request.session['user_id'] = obj.id
            if obj.usertype == 'admin':
                return HttpResponse('''<script>alert("Login successfull");window.location='HomePage'</script>''') 
            elif obj.usertype == 'user':
                return HttpResponse('''<script>alert("Login successfull");window.location='UserHomePageView'</script>''')   
            else:
                return HttpResponse('''<script>alert("Invalid User");window.location='/'</script>''')
        except LoginTable.DoesNotExist:
                return HttpResponse('''<script>alert("invalid credtionals");window.location='/'</script>''')
            
class HomePage(View):
    def get(self,request):
        return render(request,'Administration/Homepage.html')
                       
class ManageCategoriesView(View):
    def get(self,request):
        c=CategoriesTable.objects.all()
        return render(request,'Administration/Manage_categories.html',{'categories':c})
    def post(self,request):
            c=CategoriesForms(request.POST,request.FILES)
            if c.is_valid():
                c.save()
                return redirect('/ManageCategoriesView')
            
class EditCategories(View):
    def get(self,request,id):
        c=CategoriesTable.objects.get(id=id)
        return render(request,'administration/editcategories.html',{'editcategories':c})
    def post(self,request,id):
        b=CategoriesTable.objects.get(id=id)
        c=CategoriesForms(request.POST,instance=b)
        if c.is_valid():
            c.save()
            return redirect('/ManageCategoriesView')                  


class DeleteCategories(View):
    def get(self,request,id):
        c=CategoriesTable.objects.get(id=id)
        c.delete()
        return redirect('/ManageCategoriesView')     

class Userview(View):
    def get(self,request):
        c=UsersTable.objects.all()
        return render(request,'Administration/Manage_users.html',{'Users':c})  
    
class DeleteUsers(View):
    def get(self,request,id):
        c=UsersTable.objects.get(id=id)
        c.delete()
        return redirect('/Userview')     

class AnalyseReportView(View):    
    def get(self,request):
        c=AnalyseReportsTable.objects.all()
        return render(request,'Administration/View_analysereports.html',{'Reports':c})
    
class FeedbackView(View):
    def get(self,request):
        c=FeedbackTable.objects.all()
        return render(request,'Administration/View_feedback.html',{'Feedback':c})
    
class UploadPaperView(View):
    def get(self,request):
        c=UploadPapersTable.objects.all()
        return render(request,'Administration/View_Uploadpapers.html',{'Uploadpapers':c})        
    
    
    
# ========================USers===================================================

class UserHomePageView(View):
    def get(self,request):
        return render(request,'UserModule/UserHome_page.html')    
    
class UserRegistrationView(View):
    def get(self,request):
        return render(request,'UserModule/User_registration.html')
    def post(self,request):
        c=UsersForms(request.POST)
        if c.is_valid():
            reg=c.save(commit=False)
            c=LoginTable.objects.create(username=reg.email,password=request.POST['password'],usertype='user')
            reg.LOGINID=c
            reg.save()
            return redirect('/')
    
    
    
class ManageProfileView(View):
    def get(self,request):
        c=UsersTable.objects.get(LOGINID_id=request.session['user_id'])
        return render(request,'UserModule/manage_profile.html',{'manageprofile':c})
    def post(self,request,id):
        b=UsersTable.objects.get(id=id)
        c=UsersForms(request.POST,instance=b)
        if c.is_valid():
            c.save()
            return redirect('/ManageProfileView')
   
    
class UploadResearchPaperView(View):
    def get(self,request):
            c=UploadPapersTable.objects.all()
            return render(request,'UserModule/upload_research.html',{'upload':c})     
    def post(self,request):
        c=UploadForm(request.POST,request.FILES)
        if c.is_valid():
            reg=c.save(commit=False)
            c=UsersTable.objects.get(LOGINID__id=request.session['user_id'])
            reg.LOGINID=c
            reg.save()
            c.save()
            return redirect('/UploadResearchPaperView')
        
class DeleteUploadpaper(View):
    def get(self,request,id):
        c=UploadPapersTable.objects.get(id=id)
        c.delete()
        return redirect('/UploadPaperView')           
    
    
class edituser(View):
    def get(self,request,id):
        c=UsersTable.objects.get(id=id)
        return render(request,"UserModule/editprofile.html",{'editprofile':c})  
    def post(self,request,id):
        d=UsersTable.objects.get(id=id)
        c=UsersForms1(request.POST,instance=d)
        if c.is_valid():
            c.save()
            return redirect('/ManageProfileView') 
    

class AianalysisView(View):            
        def get(self,request):
            return render(request,'UserModule/ai_analysis.html')

class SendFeedbackView(View):
    def get(self,request):
        return render(request,'UserModule/send_feedback.html')
    def post(self,request):
        c=FeedbacKForms(request.POST)
        if c.is_valid():
                 reg=c.save(commit=False)
                 c=UsersTable.objects.get(LOGINID_id=request.session['user_id'])
                 reg.LOGINID=c
                 reg.save()
                 return redirect('/UserHomePageView')       
        