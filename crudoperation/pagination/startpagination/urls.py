from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.StudentList.as_view(),name="studentlist")
]