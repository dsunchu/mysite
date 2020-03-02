from django.conf.urls import url,include
from . import views

#local url file of templates_app, should return views here
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
