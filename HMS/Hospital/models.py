from django.db import models

# Create your models here.

class Pharmacy(models.Model):

    title = models.CharField(max_length=79)
    pub_date = models.DateTimeField()
    body = models.TextField()
    images = models.ImageField(upload_to='E:\NSU\10th Semester\CSE327\Project Images')


