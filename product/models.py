from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Product(models.Model):

    CONDITION_TYPE = (
        ("New", "NEW"),
        ("Used", "Used"),
    )
    # contain all product detail
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='main_product/', null=True, blank=True)
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
    viewCount = models.IntegerField(default=0)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)

    # creating slug in database by overriding the save method
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


class Category(models.Model):
    categoryName = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    category_slug = models.SlugField(blank=True, null=True)

    # creating slug in database by overriding the save method
    def save(self, *args, **kwargs):
        if not self.slug and self.categoryName:
            self.slug = slugify(self.categoryName)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.categoryName

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    brandName = models.CharField(max_length=150)

    def __str__(self):
        return self.brandName

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
