from unittest.mock import MagicMock

from api.reservations.views import reservations_table


res_table = [
    {'rental_id': 1, 'id': 1, 'checkin': '2022-01-01', 'checkout': '2022-01-13', 'previous_reserv_id': None},
    {'rental_id': 1, 'id': 2, 'checkin': '2022-01-20', 'checkout': '2022-02-10', 'previous_reserv_id': 1},
    {'rental_id': 1, 'id': 3, 'checkin': '2022-02-20', 'checkout': '2022-03-10', 'previous_reserv_id': 2},
    {'rental_id': 2, 'id': 4, 'checkin': '2022-01-02', 'checkout': '2022-01-20', 'previous_reserv_id': None},
    {'rental_id': 2, 'id': 5, 'checkin': '2022-01-20', 'checkout': '2022-01-11', 'previous_reserv_id': 4},
]


def test_reservations_table(mocker):
    mocker.patch('api.reservations.views.calculate_prev_ids', return_value=res_table)
    mock_request = MagicMock()
    assert reservations_table(mock_request) == res_table, 'Previous reservation id is incorrect'
