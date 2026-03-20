from django.db import models

class WebDesign(models.Model):
    name = models.CharField(max_length=255)
    public = models.BooleanField(default=True)
    category = models.ManyToManyField('WebDesignCategory')
    description = models.TextField(max_length=2047, default='...')
    design = models.CharField(max_length=24, unique=True, null=True)
    url = models.URLField(null=True, blank=True)
    preview = models.ImageField(upload_to='designs/images/', null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.id})'

class WebDesignCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class WebFeature(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2047, null=True)
    value = models.PositiveSmallIntegerField()
