from django.urls import resolve, reverse


def test_index_url():
    assert reverse("cart:index") == "/cart/"
    assert resolve("/cart/").view_name == "cart:index"


def test_add_product_url():
    assert reverse("cart:add_product") == "/cart/add-product/"
    assert resolve("/cart/add-product/").view_name == "cart:add_product"


def test_chage_item_count_url():
    assert reverse("cart:change_item_count") == "/cart/change-item-count/"
    assert resolve("/cart/change-item-count/").view_name == "cart:change_item_count"


def test_delete_item_url():
    assert reverse("cart:delete_item") == "/cart/delete-item/"
    assert resolve("/cart/delete-item/").view_name == "cart:delete_item"
