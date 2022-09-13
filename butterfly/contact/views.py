from django.views.generic import CreateView

from .models import Subscription
from .forms import SubscriptionForms

class SubscribeView(CreateView):
    model = Subscription
    form_class = SubscriptionForms
    success_url = "/"