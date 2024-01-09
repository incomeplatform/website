from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('sign.urls')), 
    path('', include('quetions.urls')), 
    path('', include('practice.urls')), 
 
  
    
]
