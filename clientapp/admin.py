from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Call, Category, Status, Company, CustomUser

def make_archived(modeladmin, request, queryset):
    queryset.update(is_archived=True)
make_archived.short_description = "Отправить в архив"


def make_not_archived(modeladmin, request, queryset):
    queryset.update(is_archived=False)
make_not_archived.short_description = "Убрать из архива"


class Calladmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created', 'author')
    list_filter = ('status', 'is_archived', 'category')
    search_fields = ['title', 'message']
    actions = [make_archived, make_not_archived]


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = list(UserAdmin.fieldsets) + [('Дополнительные поля', {'fields': ('company',)})]
    list_filter = ('company', 'is_staff', 'is_active')


admin.site.register(Call, Calladmin)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Company)
admin.site.register(CustomUser, CustomUserAdmin)
