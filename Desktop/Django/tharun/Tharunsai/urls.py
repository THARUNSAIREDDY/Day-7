from django.urls import path
from Tharunsai import views


urlpatterns = [
   path('',views.home),
   path('demo/',views.chk),
   path('ho/',views.homepage),
   path('logp/',views.logp),
   path('reg/',views.reg),

]