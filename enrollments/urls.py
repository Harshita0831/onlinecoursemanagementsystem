from django.urls import path
from .views import enroll_course, my_courses, update_progress

urlpatterns = [
    path('enroll/', enroll_course),
    path('my-courses/', my_courses),
    path('progress/', update_progress),
]