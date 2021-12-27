from django.db import models
import datetime
from django.db.models.fields import BooleanField
from django.template.defaultfilters import slugify # for auto-slug _  #pip install python-slugify



# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=101)
    slug = models.SlugField(max_length=150, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='%Y/%m/%d/', default='default.png', blank=True)
    # title slug date body thumb

    def __str__(self):
        return self.title
    
    def save(self): # for auto-slug __   date and title
        super(Article, self).save()
        date = datetime.datetime.now()
        self.slug = '%i-%i-%i-%s-%s-%s-%s' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second, slugify(self.title)
        )
        super(Article, self).save()

    def snippet(self):
        return self.body[:100] +'...'

class Customer(models.Model):
    name = models.CharField(max_length=80)
    active = BooleanField(default=True)

    def __str__(self):
        return str(self.name)