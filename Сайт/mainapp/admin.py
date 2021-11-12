from .models import *

from django.forms import ModelChoiceField
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='books'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class MagazineAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='magazines'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Order)
