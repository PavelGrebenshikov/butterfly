from django import template

register = template.Library()


@register.filter(name='mul')
def multiply(number: int | float, multiplier: int | float) -> int | float:
    return number*multiplier
