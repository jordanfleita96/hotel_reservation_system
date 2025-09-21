from __future__ import annotations


class ExternalPaymentSystem:
    """
    Mock external payment gateway with a different interface.
    """

    def make_payment(self, amount: float) -> dict:
        return {"status": "ok", "amount": round(float(amount), 2), "provider": "MockGateway"}


class PaymentGatewayAdapter:
    """
    Adapter Pattern: exposes process_payment(amount) using the external make_payment(amount).
    """

    def __init__(self, external_payment_system: ExternalPaymentSystem):
        self.external_payment_system = external_payment_system

    def process_payment(self, amount: float) -> dict:
        return self.external_payment_system.make_payment(amount)
