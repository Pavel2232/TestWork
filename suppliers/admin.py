from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from suppliers.models import Suppliers, RetailNetwork, IndividualEntrepreneur, Contact, Product


@admin.action(description='Очистка задолженности')
def clear_debt(modeladmin, request, queryset):
    for obj in queryset:
        obj.debt = 0
        obj.save()


class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)


class RetailNetworkAdmin(admin.ModelAdmin):
    actions = [clear_debt]
    list_display = ('title', 'provider_link', 'contact')
    list_filter = ('contact',)

    def provider_link(self, obj):
        return format_html('<a href="{}">{}</a>', reverse('admin:suppliers_suppliers_change', args=[obj.provider.id]),
                           obj.provider.title)

    provider_link.short_description = "Поставщики"


class IndividualEntrepreneurAdmin(RetailNetworkAdmin):
    pass


admin.site.register(Suppliers, SuppliersAdmin)
admin.site.register(RetailNetwork, RetailNetworkAdmin)
admin.site.register(IndividualEntrepreneur, IndividualEntrepreneurAdmin)
admin.site.register(Contact)
admin.site.register(Product)
