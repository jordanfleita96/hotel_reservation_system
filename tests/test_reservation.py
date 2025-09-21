from hotel.customer import StandardCustomer
from hotel.reservation import Reservation


class CollectingObserver:
    def __init__(self):
        self.messages = []

    def update(self, reservation):
        self.messages.append(reservation.summary_line())


def test_observer_notified_on_confirmation():
    cust = StandardCustomer("Test", "User")
    r = Reservation(
        purpose="Business",
        room_type="Single",
        num_rooms=1,
        checkin_date="2024-12-01",
        checkout_date="2024-12-05",
        payment_type="Card",
        customer=cust,
    )
    obs = CollectingObserver()
    r.add_observer(obs)

    _ = r.generate_confirmation()
    assert len(obs.messages) == 1
    assert "Single x1" in obs.messages[0]


def test_total_amount_computation():
    cust = StandardCustomer("Test", "User")
    r = Reservation(
        purpose="Business",
        room_type="Double",
        num_rooms=2,
        checkin_date="2024-12-01",
        checkout_date="2024-12-05",
        payment_type="Card",
        customer=cust,
    )
    # Double = 120 per night; 4 nights; 2 rooms => 120*4*2 = 960
    assert r.total_amount() == 960.0
