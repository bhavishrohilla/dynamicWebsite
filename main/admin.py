from django.contrib import admin

# Register your models here.
from .models import Summary, Skill, Experience, Project, Education

admin.site.register(Summary)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Education)