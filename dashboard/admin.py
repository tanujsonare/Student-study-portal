from django.contrib import admin
from .models import Note, Homework, Todo, Subject
# Register your models here.

admin.site.register(Note)
admin.site.register(Homework)
admin.site.register(Todo)
admin.site.register(Subject)
