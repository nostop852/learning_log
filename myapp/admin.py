from django.contrib import admin

# Register your models here.
from .models import Person,MyModel,Fruit
admin.site.register(Person)
admin.site.register(MyModel)
admin.site.register(Fruit)