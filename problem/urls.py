from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.problemhome,name="problemhome"),
    path('publishpage/',views.pubpage,name="publishpage"),
    path('problemtags/',views.problemtags,name="tags search"),
    path('problemtags/<str:tagname>/',views.showtags,name="problemtags"),
    path('problemtags/tag/<int:id>/',views.probdetails,name="problemDetails"),
    path('handlepubpage/',views.handlepubpage,name="handlepubpage"),
]
