from django.db import models

class Bookings(models.Model):
    flights_id = models.IntegerField(null=True)
    username = models.CharField(max_length=50)
    passport = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    payments_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'bookings'

    def __str__(self):
        return self.username