from allauth.account.signals import user_logged_in
from django.dispatch import receiver

from butterfly.cart.models import Cart


@receiver(user_logged_in)
def set_cart_owner(request, user, **kwargs):
    cart_id = request.session.get('cart_id')
    user_cart = Cart.objects.filter(user=user).first()
    if not user_cart and cart_id:
        cart = Cart.objects.get(
            pk=int(cart_id)
        )

        cart.user = user
        cart.save()

        del request.session['cart_id']


user_logged_in.connect(set_cart_owner)
