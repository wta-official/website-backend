from markdownx.admin import MarkdownxModelAdmin 
from django.contrib import admin
from .models import Blog, Booking, Category, Job, Partner, Talent, Work


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('title', 'created_at',)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',)

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)
    list_filter = ('category',)
    search_fields = ('title',)

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ('name', 'instagram', 'linkedIn', 'created_at',)
    search_fields = ('name', 'instagram', 'linkedIn',)
    filter_horizontal = ('works', 'partners',)
    list_filter = ('name', 'works')

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'created_at',)
#     search_fields = ('title', 'author',)
    
@admin.register(Blog)
class BlogAdmin(MarkdownxModelAdmin):  # ✅ change inheritance
    list_display = ('title', 'author', 'created_at',)
    search_fields = ('title', 'author',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_type', 'job_location', 'created_at',)
    search_fields = ('title', 'job_type', 'job_location')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('talent', 'fullname', 'email', 'event_name', 'event_date', 'created_at')
    search_fields = ('fullname', 'email', 'event_name', 'talent__name')
    list_filter = ('event_date', 'talent')