from django.contrib import admin
from .models import Task  # Imports your Task model

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Turns the admin list view into a neat, 4-column spreadsheet grid
    list_display = ('title', 'user', 'is_completed', 'created_at')
    
    # Adds a clickable filtering sidebar on the right side of the screen
    list_filter = ('is_completed', 'created_at')
    
    # Adds a search bar at the top to search by task title or creator's username
    search_fields = ('title', 'user__username')