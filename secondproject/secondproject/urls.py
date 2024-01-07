from django.contrib import admin
from django.urls import path
from . import views # current directory 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index)
]
# 127.0.0.1:8000 

# when we make the project, there is no views.py available we make it
# when we make an app, there is no urls.py available we make it 