"""
URL configuration for AiResearchPaper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from .views import *
# from AiResearchPaper.AiResearchapp import views

urlpatterns = [
    
# =========================Administration=========================
    
  path("",LoginView.as_view(),name="Admin_login"),
  
  path("ManageCategoriesView",ManageCategoriesView.as_view(),name="Manage_categories"),
  
  path("EditCategories/<int:id>",EditCategories.as_view(),name="EditCategories"),
  
  path("DeleteCategories/<int:id>",DeleteCategories.as_view(),name="DeleteCategories"),
  
  
  
  path("Userview",Userview.as_view(),name="Manage_users"),
  
  path("DeleteUsers/<int:id>",DeleteUsers.as_view(),name="DeleteUsers"),
  
  
  path("HomePage",HomePage.as_view(),name="Homepage"),
  
  
  path("AnalyseReportView",AnalyseReportView.as_view(),name="View_analysereports"),

  path("FeedbackView",FeedbackView.as_view(),name="View_feedback"),
    
  path("UploadPaperView",UploadPaperView.as_view(),name="View_Uploadpapers"),
    
  
#   =================================USERS VIEW==========================================

  path("UserHomePageView",UserHomePageView.as_view(),name="UserHome_page"),
   
  path("UserRegistrationView",UserRegistrationView.as_view(),name="User_registration"),  
  
  path("ManageProfileView",ManageProfileView.as_view(),name="manage_profile"),
  
  path("UploadResearchPaperView",UploadResearchPaperView.as_view(),name="upload_research"),
  
  path("AianalysisView",AianalysisView.as_view(),name="ai_analysis"),
  
  path("SendFeedbackView",SendFeedbackView.as_view(),name="send_feedback"),
  
  
  path("edituser/<int:id>",edituser.as_view(),name="editprofile"),
  
  path("DeleteUploadpaper/<int:id>",DeleteUploadpaper.as_view(),name="DeleteUploadpaper"),
  

  




  
]
