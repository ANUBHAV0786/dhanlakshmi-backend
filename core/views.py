from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Testimonial
from .models import Blog
from .serializers import BlogSerializer   # BlogResponseSerializer
from .serializers import TestimonialSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view

class TestimonialListCreateView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        testimonials = Testimonial.objects.order_by('-created_at')
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestimonialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


#######################

from .models import Contact
from .serializers import ContactSerializer

from django.core.mail import send_mail

class ContactCreateView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            # Send email notification
            subject = f"New Contact from {contact.name}"
            message = f"Subject: {contact.subject}\n\nMessage:\n{contact.message}\n\nEmail: {contact.email}"
            send_mail(subject, message, 'paenterpriseslimited@gmail.com', ['paenterpriseslimited@gmail.com'])

            return Response({'message': 'Contact message received and emailed.'}, status=201)
        return Response(serializer.errors, status=400)


######################

class BlogListView(APIView):
    def get(self, request):
        blog_type = request.GET.get('type')  # ?type=home/about/services
        if blog_type:
            blogs = Blog.objects.filter(blog_type=blog_type)
        else:
            blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

class BlogDetailView(APIView):
    def get(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=404)
# ///////////////////////        
# @api_view(['POST'])
# def blog_response_submit(request, blog_id):
#     try:
#         blog = Blog.objects.get(id=blog_id)
#     except Blog.DoesNotExist:
#         return Response({'error': 'Blog not found'}, status=404)

#     data = request.data.copy()
#     data['blog'] = blog.id

#     serializer = BlogResponseSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)