from django.contrib import admin
from .models import Testimonial
from .models import Contact
from .models import Blog  # BlogResponse


admin.site.register(Testimonial)
admin.site.register(Contact)
admin.site.register(Blog)
#admin.site.register(BlogResponse)