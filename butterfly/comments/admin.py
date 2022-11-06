from django.contrib import admin


from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["short_text", "product", "rating"]
    search_fields = ["user__username", "product__name", "rating"]

    def short_text(self, model: Comment) -> str:
        return model.text.split('.')[0] + '...'
