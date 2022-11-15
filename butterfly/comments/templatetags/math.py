from django import template

register = template.Library()

@register.filter()
def minus(value: str | int, other: str | int):
    return int(value) - int(other)
