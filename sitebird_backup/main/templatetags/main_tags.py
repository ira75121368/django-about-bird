from django import template
import main.views as views
from main.models import Categories

register = template.Library()

@register.simple_tag()
def get_categories():
    return views.cats_db

@register.inclusion_tag('main/list_categories.html')
def show_categories(cat_selected=0):
    cats = Categories.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
