from django.db import models


class Rental(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        db_table = 'rental'


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    rental = models.ForeignKey('Rental', db_column='rental_id', on_delete=models.DO_NOTHING)
    checkin = models.DateField(blank=True, null=True)
    checkout = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'reservations'
