from django.urls import path,include
from .import views
 

urlpatterns = [
   path('issues/',views.supportticket,name="support")
]