from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    # photos folder will be created
    photo = models.ImageField(upload_to='photos/%Y/%m/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add = True)

    # when you create a function inside a class - you have to put "self"
    # damit kein "Object(1) oder so angezeigt wird
    def __str__(self):
        return self.first_name

    # Programm macht automatisch Plural, das wollen wir nicht
   # class Meta:
   #    verbose_name_plural = 'Teams'