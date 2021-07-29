from django.shortcuts import render
from django.views.generic import (View,TemplateView,
	ListView,DetailView,
	CreateView,UpdateView,DeleteView)
from . import models
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class IndexView(TemplateView):
	template_name='index.html'


class SchoolListView(ListView):
	model = models.School
	context_object_name='Schools'
	template_name='basic_app/school_list.html'
class SchoolDetailView(DetailView):
	context_object_name='School_detail'
	model = models.School
	template_name = 'basic_app/school_details.html'
class SchoolCreateView(CreateView):
	fields=('name','principal','location')
	model= models.School
	template_name='basic_app/school_forms.html'
	success_url=reverse_lazy("basic_app:list")
class SchoolUpdateView(UpdateView):
	fields=('name','principal')
	model=models.School
	template_name='basic_app/school_update.html'
class SchoolDeleteView(DeleteView):
	model=models.School
	template_name='basic_app/school_delete.html'
	success_url=reverse_lazy("basic_app:list")

class StudentCreateView(CreateView):
	fields=('name','age','school')
	model= models.Student
	success_url=reverse_lazy("basic_app:list")
	template_name='basic_app/student_forms.html'



