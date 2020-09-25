from django.db import models
from .slugify import slugify
from ..users.models import User


class Image(models.Model):
    path = models.ImageField(upload_to='images/',)

    def __str__(self):
        return self.path.name


class GoalOfSupport(models.Model):
    name = models.CharField(max_length=52,  null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self', blank=True, null=True,
        related_name='children', on_delete=models.CASCADE
    )
    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"      # categories under a parent with same

    def __str__(self):
        full_path = [self.name]
        parent = self.parent

        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent

        return ' -> '.join(full_path[::-1])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class HotCategories(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    icon = models.ForeignKey(Image, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class City(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', blank=True, null=True,
        related_name='children', on_delete=models.CASCADE
    )
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        full_path = [self.name]
        parent = self.parent

        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent

        return ' -> '.join(full_path[::-1])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class SendToEmail(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    to_email = models.EmailField()
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)


class StatusProduct(models.Model):
    name = models.CharField(max_length=15)
