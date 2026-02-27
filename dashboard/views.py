from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg, Count
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from accounts.models import User
from courses.models import Course, Module, Lecture
from enrollments.models import Enrollment
from reviews.models import Review


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_summary(request):
    total_users = User.objects.count()
    total_courses = Course.objects.count()
    total_enrollments = Enrollment.objects.count()

    avg_rating = Review.objects.aggregate(avg=Avg('rating'))['avg']
    top_courses = (
        Enrollment.objects
        .values('course__title')
        .annotate(total=Count('id'))
        .order_by('-total')[:5]
    )

    data = {
        "total_users": total_users,
        "total_courses": total_courses,
        "total_enrollments": total_enrollments,
        "average_rating": avg_rating,
        "top_courses": list(top_courses),
    }

    return Response(data)

def home(request):
    return render(request, "home.html")


def courses_page(request):
    courses = Course.objects.filter(is_published=True)
    return render(request, "course-list.html", {"courses": courses})


@login_required
def dashboard(request):
    user_obj = get_object_or_404(User, id=request.user.id)

    total_courses = Course.objects.filter(is_published=True).count()
    total_modules = Module.objects.count()
    total_lectures = Lecture.objects.count()

    enrolled_courses = Enrollment.objects.filter(
        student=user_obj
    ).select_related("course")

    context = {
        "total_courses": total_courses,
        "total_modules": total_modules,
        "total_lectures": total_lectures,
        "students": 58,
        "enrolled_courses": enrolled_courses,
    }

    return render(request, "dashboard.html", context)


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("home")


def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    modules = Module.objects.filter(course=course).order_by("order")

    is_enrolled = False

    if request.user.is_authenticated:
        user_obj = get_object_or_404(User, id=request.user.id)

        is_enrolled = Enrollment.objects.filter(
            student=user_obj,
            course=course
        ).exists()

    return render(request, "course-detail.html", {
        "course": course,
        "modules": modules,
        "is_enrolled": is_enrolled
    })


@login_required
def enroll_course(request, id):
    course = get_object_or_404(Course, id=id)
    user_obj = get_object_or_404(User, id=request.user.id)

    Enrollment.objects.get_or_create(
        student=user_obj,
        course=course
    )

    return redirect("course-detail", id=id)