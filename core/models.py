from django.db import models


  
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}'s Testimonial"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"


class Blog(models.Model):
    BLOG_TYPES = (
        ('home', 'Home Page'),
        ('about', 'About Us Page'),
        ('services', 'Services Page'),
    )

    title = models.CharField(max_length=200)
    image = models.URLField()
    content = models.TextField()
    blog_type = models.CharField(max_length=20, choices=BLOG_TYPES)

    def __str__(self):
        return self.title
    


# class BlogResponse(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='responses')
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()

#     submitted_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} → {self.blog.title}"
