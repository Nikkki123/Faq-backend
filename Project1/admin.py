from django.contrib import admin
from .models import TodoItem
from .models import FAQ
# Register your models here.
admin.site.register(TodoItem)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    admin.site.register(FAQ)
