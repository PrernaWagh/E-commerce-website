from django.contrib import admin
from .models import Product,Order

'''
Admin Panel Customization
'''

# Changing admin site header
admin.site.site_header = "E-Commerce Site"
# Adding title to page
admin.site.site_title = "ShoppyZ"
# changing index title
admin.site.index_title = "Manage ShppyZ Shopping"

class ProductAdmin(admin.ModelAdmin):
    # Adding function to change category to default
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")
    
    change_category_to_default.short_description = "Default Category"
    list_display = ('title', 'category', 'description', 'price', 'discount_price') # Displaying extra fields than title.
    search_fields = ('title', 'category') # Adding search field on page
    actions = ('change_category_to_default',)
    fields = ('title', 'price', 'category', 'description', 'discount_price','image') # Changing order of fields
    list_editable = ('price', 'category')    


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)