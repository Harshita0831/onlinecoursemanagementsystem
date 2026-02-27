from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
import email


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        email = request.query_params.get('email')
        full_name = request.query_params.get('full_name')
        role = request.query_params.get('role')

        if email:
            users = users.filter(email__icontains=email)
        if full_name:
            users = users.filter(full_name__icontains=full_name)
        if role:
            users = users.filter(role=role)

        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(users, request)

        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
