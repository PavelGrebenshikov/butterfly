from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["username", "items_count"]
    search_fields = ["user__username"]
    inlines = [OrderItemInline]
    readonly_fields = ["created_at"]

    def items_count(self, model: Order) -> int:
        return model.items.count()

    def username(self, model: Order) -> str:
        return model.user


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["username", "product", "count"]
    search_fields = ["order__user__username", "product__name"]

    def username(self, model: OrderItem) -> str:
        return model.order.user
