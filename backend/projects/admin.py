from django.contrib import admin
from projects.models import Project, Pledge


@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    pass

@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    pass
