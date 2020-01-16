from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm
from .models import CustomUser
# Register your models here.

class UserAdmin(BaseUserAdmin):
	add_form = UserCreationForm

	list_display = ('username','email','team_num', 'VID', 'is_admin', 'is_staff', 'is_active')
	list_filter = ('is_admin', 'is_staff', 'is_active', 'team_num')

	fieldsets = (
			(None, {'fields': ('username','email','password', 'team_num')}),
			('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')})
		)
	search_fields = ('username','email', 'team_num')
	ordering = ('username','email', 'team_num')

	filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
#admin.site.register(Profile)
admin.site.unregister(Group)