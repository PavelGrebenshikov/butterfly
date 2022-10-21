from django.urls import resolve, reverse


def test_index_url():
    assert reverse("orders:index") == "/orders/"
    assert resolve("/orders/").view_name == "orders:index"


def test_create_url():
    assert reverse("orders:create") == "/orders/create/"
    assert resolve("/orders/create/").view_name == "orders:create"


def test_approve_payment_url():
    assert reverse("orders:approve_payment") == "/orders/approve-payment/"
    assert resolve("/orders/approve-payment/").view_name == "orders:approve_payment"
