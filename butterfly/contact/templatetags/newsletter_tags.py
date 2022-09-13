from django import template

from butterfly.contact.forms import SubscriptionForms


register = template.Library()

@register.inclusion_tag("contact/tags/forms.html")
def newsletter_form():
    return {"newsletter_form": SubscriptionForms()}