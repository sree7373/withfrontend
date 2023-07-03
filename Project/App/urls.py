from django.urls import path
from .views import *

urlpatterns = [
    
    # path ('login/',login, name='login'),
    
    path ('employee_details/',employee_details, name='employee_details'),
    
    path('success/', success, name='success'),
    
]