from django import template

register = template.Library()

@register.filter(name='ifinlist')
def ifinlist(value, values):
    return value in values

