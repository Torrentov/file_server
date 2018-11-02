from django.db import models


class Document(models.Model):
    PATH = ''
    docfile = models.FileField(upload_to=PATH)