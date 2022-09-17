from django import template

register = template.Library()


@register.filter(name="gettype")
def gettype(obj) -> str:
    return type(obj).__name__
