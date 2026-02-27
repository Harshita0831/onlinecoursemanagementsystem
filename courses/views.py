from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import Course, Category
from .serializers import CourseSerializer, CategorySerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@cache_page(60)
def course_list(request):

    if request.method == 'GET':
        courses = Course.objects.all()

        title = request.query_params.get('title')
        level = request.query_params.get('level')
        category = request.query_params.get('category')

        if title:
            courses = courses.filter(title__icontains=title)
        if level:
            courses = courses.filter(level=level)
        if category:
            courses = courses.filter(category__id=category)

        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(courses, request)

        serializer = CourseSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_detail(request, pk):

    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({"error":"Course not found"}, status = 404)
    
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        course.delete()
        return Response({"message": "Course deleted"}, status=204)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def category_list(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def instructor_courses(request):

    courses = Course.objects.filter(instructor=request.user)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)