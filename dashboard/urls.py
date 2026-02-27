from django.urls import path
from .views import home, courses_page, dashboard, login_page, course_detail, enroll_course, logout_user

urlpatterns = [
    path('', home, name="home"),
    path('courses/', courses_page, name="courses"),
    path('login/', login_page, name="login"),
    path("logout/", logout_user, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('courses/<int:id>/', course_detail, name="course-detail"),
    path('courses/<int:id>/enroll/', enroll_course, name="enroll-course"),
]