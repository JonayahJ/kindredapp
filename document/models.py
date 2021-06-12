from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Document(models.Model):
    title       = models.CharField(max_length=255)
    # content     = models.TextField(blank=True, null=True)
    content     = RichTextField(blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title