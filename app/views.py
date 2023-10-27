from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Student
from .forms import StudentForm

# Create your views here.
class StartPageView(ListView):
    template_name = 'app/index.html'
    model = Student


class StudentDetailView(DetailView):
    template_name = 'app/detail.html'
    model = Student
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    template_name = 'app/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_list')

