from django.urls import path


from .views import TestimonialListCreateView, ContactCreateView
from .views import BlogListView, BlogDetailView #blog_response_submit

urlpatterns = [
  
    path('testimonials/', TestimonialListCreateView.as_view()),
    path('contact/', ContactCreateView.as_view()),  
    path('blogs/', BlogListView.as_view()),
    path('blogs/<int:blog_id>/', BlogDetailView.as_view()),
    #path('blogs/<int:blog_id>/respond/', blog_response_submit),
]

