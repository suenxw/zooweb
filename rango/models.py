from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class AnimalCategory(models.Model):
    NAME_MAX_LENGTH = 128

    category_name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(AnimalCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Animal Categories'

    def __str__(self):
        return self.category_name


class Animal(models.Model):
    NAME_MAX_LENGTH = 128

    animal_name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    category = models.ForeignKey(AnimalCategory, on_delete=models.CASCADE)

    size = models.TextField()
    distribution_area = models.TextField()

    likes = models.IntegerField(default=0)
    brief = models.TextField()
    picture = models.ImageField(upload_to='animals_images', blank=True)

    def __str__(self):
        return self.animal_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]
