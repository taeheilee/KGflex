from django.db import models
from django.contrib.auth.models import User
import os
from imagekit.models import  ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class KGflex(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()
  file_upload = models.FileField(upload_to='KGflex/data/%Y/%m/%d/', blank=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
    return f'[PK:{self.pk}]-{self.title} :: {self.author}'

  def get_FileName(self):
    return os.path.basename(self.file_upload.name)

  def get_absolute_url(self):
    return f'/KGflex/free/{self.pk}/'


class Notice(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()
  file_upload = models.FileField(upload_to='KGflex/data/%Y/%m/%d/', blank=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
    return f'[PK:{self.pk}]-{self.title} :: {self.author}'

  def get_FileName(self):
        return os.path.basename(self.file_upload.name)

  def get_absolute_url(self):
    return f'/KGflex/notice/{self.pk}/'    


class KDrama(models.Model):
  title = models.CharField(max_length=30)
  name = models.CharField(max_length=30, null=True, blank=True)
  content = models.TextField()
  file_upload = models.FileField(upload_to='KGflex/KDrama/')
  photo = models.ImageField(upload_to = 'blog/KDrama')
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
    return f'[PK:{self.pk}]-{self.title} :: {self.author}'

  def get_FileName(self):
        return os.path.basename(self.file_upload.name)

  def get_absolute_url(self):
    return f'/KGflex/KDrama/{self.pk}/'    







class entertainment(models.Model):
  title = models.CharField(max_length=30)
  name = models.CharField(max_length=30, null=True, blank=True)
  content = models.TextField()
  file_upload = models.FileField(upload_to='KGflex/entertainment/')
  photo = models.ImageField(upload_to = 'blog/entertainment')
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
    return f'[PK:{self.pk}]-{self.title} :: {self.author}'

  def get_FileName(self):
        return os.path.basename(self.file_upload.name)

  def get_absolute_url(self):
    return f'/KGflex/entertainment/{self.pk}/'    






class KMovie(models.Model):
  title = models.CharField(max_length=30)
  name = models.CharField(max_length=30, null=True, blank=True)
  content = models.TextField()
  file_upload = models.FileField(upload_to='KGflex/KMovie/')
  photo = models.ImageField(upload_to = 'blog/KMovie')
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
    return f'[PK:{self.pk}]-{self.title} :: {self.author}'

  def get_FileName(self):
        return os.path.basename(self.file_upload.name)

  def get_absolute_url(self):
    return f'/KGflex/KMovie/{self.pk}/'    





class UMovie(models.Model):
  title = models.CharField(max_length=30)
  name = models.CharField(max_length=30, null=True, blank=True)
  content = models.TextField()
  file_upload = models.FileField(upload_to='KGflex/UMovie/')
  photo = models.ImageField(upload_to = 'blog/UMovie')
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
    return f'[PK:{self.pk}]-{self.title} :: {self.author}'

  def get_FileName(self):
        return os.path.basename(self.file_upload.name)

  def get_absolute_url(self):
    return f'/KGflex/UMovie/{self.pk}/'    







    

  