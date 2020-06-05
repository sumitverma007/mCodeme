from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.memehome,name="memehome"),
    path('postComment/',views.postComment,name="handlecomment"),
    path('<str:slug>/<int:id>',views.memdetail,name="memdetail"),
    path('<str:slug>/',views.memetag,name="memetag"),

]
