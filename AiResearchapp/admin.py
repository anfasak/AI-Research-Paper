from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(UsersTable)
admin.site.register(CategoriesTable)
admin.site.register(AnalyseReportsTable)
admin.site.register(FeedbackTable)
admin.site.register(UploadPapersTable)