from django.urls import path  
from . import views 

# This is the URL configuration for the calc app
#have to import views our url will be mapped to /add ...

urlpatterns =[  # This is a dictionary specify mapping
    
    path('register',views.register, name='register'),  # If the path is empty, go to the home view (can make it index.html too later on)
    path('login', views.login, name='login'),  # If the path is add, go to the add view
    path('logout', views.logout, name='logout')  # If the path is add, go to the add view
]
 







