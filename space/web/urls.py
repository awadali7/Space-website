from operator import index
from django.urls import path, include
from web.views import index


urlpatterns = [
    path("",index)
]
