from django.contrib import admin
from .models import Post

# Registering model so it can show up on admin page
admin.site.register(Post)
