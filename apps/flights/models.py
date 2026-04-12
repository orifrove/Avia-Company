from django.db import models

class Flight(models.Model):
    number_of_race = models.CharField(max_length=100)
    flight_date = models.CharField(max_length=50)
    flight_time = models.CharField(max_length=50)
    from_city = models.CharField(max_length=25)
    to_city = models.CharField(max_length=25)
    aircraft_id = models.IntegerField(null=True)
    bookings_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'flights'

    def __str__(self):
        return self.number_of_race
