from django.contrib import admin
from .models import Blog, Category, Partner, Talent, Work


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('title',)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('category',)
    search_fields = ('title',)

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ('name', 'instagram', 'linkedIn',)
    search_fields = ('name', 'instagram', 'linkedIn',)
    filter_horizontal = ('works', 'partners',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    search_fields = ('title', 'author',)