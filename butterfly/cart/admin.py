from django.contrib import admin

from .models import Cart, CartItem


class CartItemInline(admin.StackedInline):
    model = CartItem
    extra = 3


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['username', 'items_count']
    search_fields = ['user__username']
    inlines = [CartItemInline]
    readonly_fields = ['created_at']

    def items_count(self, model: Cart) -> int:
        return model.items.count()

    def username(self, model: Cart) -> str:
        return model.user if model.user else '<anonymous>'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['username', 'product', 'count']
    search_fields = ['cart__user__username', 'product__name']

    def username(self, model: CartItem) -> str:
        return model.cart.user if model.cart.user else '<anonymous>'
