from django.contrib import admin
from .models import Join



class JoinAdmin(admin.ModelAdmin):
    """ join admin customisation """
    list_display = ('email_address', 'friend', 'created_date', 'update_date', 'slug', )
    list_filter = ('created_date',)
    search_fields = ('first_name', 'friend', 'email',)
    prepopulated_fields = {'slug': ('first_name',)}
# Register your models here.
admin.site.register(Join, JoinAdmin)

