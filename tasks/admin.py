from django.contrib import admin
from .models import Worker, Task, Project, TimeLog, Comment

# Register your models here.
admin.site.register(Worker)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(TimeLog)
admin.site.register(Comment)