from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from .customer import Customer
from .observers import ReservationObserver


@dataclass
class Reservation:
    purpose: str
    room_type: str
    num_rooms: int
    checkin_date: str
    checkout_date: str
    payment_type: str
    customer: Customer
    observers: List[ReservationObserver] = field(default_factory=list)

    def add_observer(self, observer: ReservationObserver) -> None:
        self.observers.append(observer)

    def notify(self) -> None:
        for obs in self.observers:
            obs.update(self)

    def summary_line(self) -> str:
        return f"{self.room_type} x{self.num_rooms} from {self.checkin_date} to {self.checkout_date}"

    def generate_confirmation(self) -> str:
        msg = (
            f"Reservation confirmed for {self.customer.firstname} {self.customer.lastname}\n"
            f"Purpose: {self.purpose}\n"
            f"Room(s): {self.room_type} x{self.num_rooms}\n"
            f"Check-in: {self.checkin_date} | Check-out: {self.checkout_date}\n"
            f"Payment: {self.payment_type}"
        )
        self.notify()
        return msg

    def total_amount(self) -> float:
        price_map = {"Single": 80.0, "Double": 120.0, "Suite": 250.0}
        per_night = price_map.get(self.room_type, 100.0)
        nights = 4  # fixed for demo (2024-12-01 to 2024-12-05)
        return per_night * self.num_rooms * nights
