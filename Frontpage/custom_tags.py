# templatetags/custom_tags.py

from django import template

register = template.Library()

@register.filter
def get_sizes(product, category):
    return getattr(product, f'{category}_sizes').all()
