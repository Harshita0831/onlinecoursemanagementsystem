from django.urls import path
from .views import course_list, course_detail,  category_list, instructor_courses

urlpatterns = [
    path('courses/', course_list, name='course-list'),
    path('courses/<int:pk>/', course_detail, name='course-detail'),
    path('caegories/', category_list, name = 'category-list'),
    path('instructor/courses/', instructor_courses, name='instructor-courses'),
]