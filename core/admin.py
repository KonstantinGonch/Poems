from django.contrib import admin

from .models import Poem, Category

admin.site.register(Poem)
admin.site.register(Category)
