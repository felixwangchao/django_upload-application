from django.db import models

class Editor(models.Model):
    Editor = models.CharField(max_length = 40)
    PublicationTitle = models.CharField(max_length = 40)
    Title = models.CharField(max_length = 40)
    Name = models.CharField(max_length = 20)
    Surname = models.CharField(max_length = 20)
    Email = models.CharField(max_length = 40)
    InternationalPhoneNumber = models.CharField(max_length = 20)
        



