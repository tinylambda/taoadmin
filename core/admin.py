from django.contrib import admin


# Register your models here.
from core.models import Class, Attr


class AttrInline(admin.TabularInline):
    model = Attr
    extra = 0
    fields = ('name_human', 'name', 'dtype', 'hint')
    ordering = ('time_added',)
    show_full_result_count = True
    show_change_link = True


class ClassAdmin(admin.ModelAdmin):
    inlines = [AttrInline, ]

    list_display = ('name_human', 'name', 'hint', 'time_updated', 'time_added')
    ordering = ('-time_added', )


admin.site.register(Class, ClassAdmin)


class AttrAdmin(admin.ModelAdmin):
    pass


admin.site.register(Attr, AttrAdmin)
