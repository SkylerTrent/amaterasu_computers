from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)
    chipset = models.CharField(max_length=254)
    size = models.TextField()
    speed = models.TextField()
    vram = models.CharField(max_length=254)
    schedule_required = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.name
