from django.conf.urls import url
from employee import views

urlpatterns = [
    url('plant', views.plant, name='plant'),
]
