from django.contrib import admin
from contactbook.models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['first_name', 'last_name']}),
        ('Email', {'fields': ['email']}),
        # ('Date information', {'fields': ['add_date']}),
    ]

    list_display = ('first_name', 'last_name', 'email')
    list_filter = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

admin.site.register(Contact, ContactAdmin)