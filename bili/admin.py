from django.contrib import admin

# Register your models here.
from .models import Chapter
from .models import Entry
from .models import Exercise

admin.site.register(Chapter)
admin.site.register(Entry)
admin.site.register(Exercise)