from django.db import models

class Aircraft(models.Model):
    models = models.CharField(max_length=25)

    class Meta:
        db_table = 'aircraft'

    def __str__(self):
        return self.models