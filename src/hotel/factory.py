from __future__ import annotations
from .customer import StandardCustomer, PremiumCustomer, Customer


class CustomerFactory:
    """
    Factory Pattern: centralizes logic for constructing customers.
    """

    @staticmethod
    def create_customer(firstname: str, lastname: str, loyalty_status: str = "Standard") -> Customer:
        status = (loyalty_status or "Standard").strip().lower()
        if status == "premium":
            return PremiumCustomer(firstname, lastname, rewards_points=100)
        return StandardCustomer(firstname, lastname)
