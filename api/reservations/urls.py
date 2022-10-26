from django.conf.urls import url

from api.reservations import views

urlpatterns = [
    url(r'^table/?$', views.reservations_table, name='reservations_table'),
]
