from django import template
from app.models import WhiskyList

register = template.Library()

@register.inclusion_tag('app/categories.html')
def get_category_list(current_category=None):
    return {'categories': WhiskyList.objects.all(),
            'current_category': current_category}
