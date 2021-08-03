from django.contrib import admin
from rango.models import AnimalCategory, Animal, Comment
from rango.models import UserProfile


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('animal_name', 'category', 'brief')


class AnimalCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}


class CommentsAdmin(admin.ModelAdmin):
    comment_field = ('username', 'animal', 'email', 'content')


admin.site.register(AnimalCategory, AnimalCategoryAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment,CommentsAdmin)
