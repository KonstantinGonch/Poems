from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Poem(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class PageContent(models.Model):
    TARGET_PAGES = (("contacts", "Контакты"), ("bio", "Обо мне"), ("portal", "О портале"))

    target_page = models.CharField(max_length=50, choices=TARGET_PAGES)
    page_content = HTMLField(default="")
