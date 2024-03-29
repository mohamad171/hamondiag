from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.urls import reverse_lazy


class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(get_random_string(15))
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(blank=True, unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(get_random_string(15))
        return super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class MeasureType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="media")
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    measure_type = models.ForeignKey(MeasureType,on_delete=models.SET_NULL,null=True)
    updated = models.DateTimeField(auto_now=True)
    count_buy = models.PositiveIntegerField(default=0)
    discount = models.IntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(100)
    ], null=True, blank=True)
    category = models.ManyToManyField(to=Category, blank=True, related_name="products")
    tags = models.ManyToManyField(to=Tag, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(get_random_string(15))
        return super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("product:product-detail", args=[self.id])


class Image(models.Model):
    image = models.ImageField(upload_to="media")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="carts")
    is_paid = models.BooleanField(default=False)
    is_open = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        total_price = 0
        for pack in self.cart_products.all():
            price = pack.product.price
            if pack.product.discount:
                price = (100 - pack.product.discount) / 100 * price
            total_price += pack.count * price
        return total_price

    def __str__(self):
        return str(self.user)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
