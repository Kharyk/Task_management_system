from django.contrib import admin
from system.models import Task, Comment, Project, User

class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'creator_of_project', 'members', 'description', 'image', 'link', 'status')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "members":
            kwargs["queryset"] = User.objects.all()  
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    
    filter_horizontal = ('members',)

admin.site.register(Project, ProjectAdmin)

admin.site.register(Task)
admin.site.register(Comment)


# Register your models here.
