from django.db import models

class Payments(models.Model):
    type_fly = models.CharField(max_length=25)
    price = models.FloatField()

    class Meta:
        db_table = 'payments'

    def __str__(self):
        return self.type_fly
