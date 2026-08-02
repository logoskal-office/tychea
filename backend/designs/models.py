import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

class Design(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='designs/thumbnails/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sectors = models.ManyToManyField('Sector', related_name='designs')
    link = models.BooleanField(default=False)
    url = models.URLField(max_length=200, null=True, blank=True)
    pinned = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    public = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Design'
        verbose_name_plural = 'Designs'
        ordering = ['-pinned', '-created_at']
    
    def clean(self):
        super().clean()
        if self.link and not self.url:
            raise ValidationError({'url': 'URL field is required when link is checked.'})

    def __str__(self):
        return self.name

class Sector(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Linker(models.Model):
    name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=40, null=True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        verbose_name = 'Linker'
        verbose_name_plural = 'Linkers'

    def __str__(self):
        return f"{self.name}"