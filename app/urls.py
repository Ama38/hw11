from django.urls import path
from .views import *

urlpatterns = [
    path('', StartPageView.as_view(), name='student_list'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('create/', StudentCreateView.as_view(), name='create_student')
]