# Django Modules
from django.contrib import admin
from .models import Project, Task, Comment

def soft_delete(modeladmin, request, queryset):
    for obj in queryset:
        obj.delete()
soft_delete.short_description = "Soft delete selected items"

def soft_delete_cascade(modeladmin, request, queryset):
    for obj in queryset:
        obj.delete(soft = True, cascade = True)
soft_delete_cascade.short_description = "Soft delete selected items with cascade"


def restore(modeladmin, request, queryset):
    for obj in queryset:
        obj.restore()
restore.short_description = "Restore selected items"

def hard_delete(modeladmin, request, queryset):
    for obj in queryset:
        obj.hard_delete()
hard_delete.short_description = "Permanently delete selected items"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('is_deleted', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    actions = [soft_delete, restore, hard_delete]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'is_completed', 'due_date', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('is_deleted', 'is_completed', 'due_date', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'project__name')
    actions = [soft_delete, restore, hard_delete]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'content', 'created_at', 'is_deleted')
    list_filter = ('is_deleted', 'created_at')
    search_fields = ('content', 'task__title')
    actions = [soft_delete, restore, hard_delete]

