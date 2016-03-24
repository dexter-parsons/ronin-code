from django.contrib import admin

# Register your models here.
from .models import Goals
# Register your models here.

class GoalsAdmin(admin.ModelAdmin):
	class Meta:
		model = Goals
admin.site.register(Goals, GoalsAdmin)