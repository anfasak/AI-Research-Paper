from django.forms.models import ModelForm

from .models import *


class UsersForms(ModelForm):
    class Meta:
        model=UsersTable
        fields=['name','phone','email','LOGINID']
        
        
class UsersForms1(ModelForm):
    class Meta:
        model=UsersTable
        fields=['name','phone','email']
        
        
class CategoriesForms(ModelForm):
    class Meta:
        model=CategoriesTable
        fields=['categoryName','categoryDescription','papercount','Image']
                

class UploadForm(ModelForm):
    class Meta:
        model=UploadPapersTable
        fields=['LOGINID','title','categories','description','files']
        
class FeedbacKForms(ModelForm):
    class Meta:
        model=FeedbackTable
        fields=['feedback','Rating']        

    
        


