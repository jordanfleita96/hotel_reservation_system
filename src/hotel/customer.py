from __future__ import annotations
from abc import ABC, abstractmethod


class Customer(ABC):
    """
    Base Customer with encapsulated (protected) fields and an abstract rewards API.
    Demonstrates encapsulation and abstraction.
    """

    def __init__(self, firstname: str, lastname: str, passport_num: str | None = None):
        self._firstname = firstname
        self._lastname = lastname
        self._passport_num = passport_num  # encapsulated (protected)

    @property
    def firstname(self) -> str:
        return self._firstname

    @property
    def lastname(self) -> str:
        return self._lastname

    def get_passport_num(self) -> str | None:
        """Encapsulated accessor for sensitive data."""
        return self._passport_num

    @abstractmethod
    def calculate_rewards(self) -> str:
        """Polymorphic rewards calculation/description."""
        raise NotImplementedError


class StandardCustomer(Customer):
    """Concrete customer with basic rewards behavior."""

    def calculate_rewards(self) -> str:
        return "Standard rewards: 1 point per night."


class PremiumCustomer(Customer):
    """Concrete customer with enhanced rewards behavior."""

    def __init__(self, firstname: str, lastname: str, rewards_points: int = 0, passport_num: str | None = None):
        super().__init__(firstname, lastname, passport_num)
        self.rewards_points = rewards_points

    def calculate_rewards(self) -> str:
        return f"Premium rewards: 2 points per night (current balance: {self.rewards_points})."
