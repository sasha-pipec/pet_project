from django import template

register = template.Library()

@register.filter
def crat(value):
    if int(value)%4==0:
        return True
    else:
        return False
