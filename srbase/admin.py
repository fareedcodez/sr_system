from django.contrib import admin

# Register your models here.
from .models import Repository, College, Title

admin.site.register(Repository)
admin.site.register(College)
admin.site.register(Title)

