from rest_framework import serializers
from .models import Testimonial
from .models import Blog #BlogResponse
from .models import Contact

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

# class BlogResponseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlogResponse
#         fields = '__all__'
#         read_only_fields = ['id', 'submitted_at', 'blog']