from django.views.generic import CreateView

from .models import Mail
from .forms import SubscriptionForms

class SubscribeView(CreateView):
    model = Mail
    form_class = SubscriptionForms
    success_url = "/"