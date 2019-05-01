from django.contrib import admin

from .models import Poem, Category, PageContent

admin.site.register(Poem)
admin.site.register(Category)
admin.site.register(PageContent)
