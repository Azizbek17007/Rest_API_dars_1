from django.contrib import admin


from restApi.models import Todo


# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'is_done')
    list_display_link = ('id','title', 'description',)
    list_filter = ('title',)
    search_fields = ('title',)
    readonly_fields = ('id',)

