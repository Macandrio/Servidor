from django.urls import path,re_path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path("proyecto/", views.dame_proyecto,name="dame_proyecto"),
]