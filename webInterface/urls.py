from django.contrib import admin

from django.urls import include, path

from webInterface.views import index_view

urlpatterns = [
   
    path('', index_view,name="index_view" ),
]