from django.urls import path, include
from . import views
from .views import CourseDetailView, CourseListView

urlpatterns = [
    path('', views.index),
    path('courses_f', views.list_courses, name='courses'),
    path('courses', CourseListView.as_view(), name='courses'),
    path('course_f/<int:pk>', views.course, name="course"),
    path('course/<int:pk>', CourseDetailView.as_view(), name="course")

]