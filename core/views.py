from core.models import Course
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core import models


def index(request):
    count = Course.objects.count()
    return render(request, 'index.html', {"count": count})


def list_courses(request):
    сourses = models.Course.objects.all()
    return render(request, 'сourses.html', {"object_list": сourses})


def course(request, pk):
    сourse = models.Course.objects.get(id=pk)
    return render(request, 'сourse.html', {"object": сourse})


class CourseListView(ListView):
    model = Course
    template_name = "сourses.html"


class CourseDetailView(DetailView):
    model = Course
    template_name = "сourse.html"


