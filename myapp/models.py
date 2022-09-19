from django.db import models
from django import forms
# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    
    def __str__(self):
        return self.first_name + self.last_name

    
class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    
def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])
    def save(self, *args, **kwargs):   # 重写save方法是关键
        try:
            self.full_clean()   
        except ValidationError as e:
            print('模型验证没通过： %s' % e.message_dict)
class MyForm(forms.Form):
    even_field = forms.IntegerField(validators=[validate_even])
    
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline