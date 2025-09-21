from __future__ import annotations
from typing import Protocol


class ReservationObserver(Protocol):
    def update(self, reservation) -> None:  # protocol signature
        ...


class EmailObserver:
    def update(self, reservation) -> None:
        customer_name = f"{reservation.customer.firstname} {reservation.customer.lastname}"
        print(f"[Email] Reservation confirmed for {customer_name} - {reservation.summary_line()}")


class SMSObserver:
    def update(self, reservation) -> None:
        customer_name = f"{reservation.customer.firstname} {reservation.customer.lastname}"
        print(f"[SMS] Reservation confirmed for {customer_name} - {reservation.summary_line()}")
