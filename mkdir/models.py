from django.db.models import CharField, Model


class Text(Model):
    folder = CharField(max_length=128)