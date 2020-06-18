from django.contrib import admin

from .models import Item, Tag


class ItemAdmin(admin.ModelAdmin):
	model = Item
	list_display = ('text', 'created_on', 'modified_on', 'tags')
	fieldsets = (
		(
			'Basic Information', { 'fields': ('text',) }
		),
	)


admin.site.register(Item, ItemAdmin)