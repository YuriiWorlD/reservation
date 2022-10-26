from django.db.models import F, Window, Case, When, IntegerField
from django.db.models.functions import Lag

from api.reservations.models import Reservation


def calculate_prev_ids():
    result_table = Reservation.objects.all().order_by('id').annotate(
        prev_id=Window(
            expression=Lag('id', offset=1),
            partition_by=[F('rental')],
        ),
        prev_checkout=Window(
            expression=Lag('checkout', offset=1),
            partition_by=[F('rental')],
        ),
        previous_reserv_id=Case(When(checkin__gte=F('prev_checkout'), then=F('prev_id')),
                                output_field=IntegerField(),
                                )
    )
    return result_table


def reservations_table(request):
    resp = calculate_prev_ids()
    return list(resp)
