from django import template
from rango.models import AnimalCategory

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    return {'categories': AnimalCategory.objects.all(),
            'current_category': current_category}