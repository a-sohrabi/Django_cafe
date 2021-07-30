from django.contrib import admin
from .models import Table, MenuItems, Orders, Receipts, User

# Register your models here.


@admin.register(MenuItems)
class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('category', 'price', 'name')
    list_filter = ('price', 'category', )
    list_editable = ('price',)
    search_fields = ('name',)


# admin.site.register(Table)
# admin.site.register(MenuItems)
# admin.site.register(Orders)
# admin.site.register(Receipts)
# admin.site.register(User)
