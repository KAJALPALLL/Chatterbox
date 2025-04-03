from django.urls import path
from . import views

urlpatterns = [

    path('',views.chat_view,name='chat_view'),
    path('file',views.upload_file,name='upload_file'),

]

