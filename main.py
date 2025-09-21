from hotel.customer import StandardCustomer, PremiumCustomer
from hotel.factory import CustomerFactory
from hotel.observers import EmailObserver, SMSObserver
from hotel.reservation import Reservation
from hotel.adapter import ExternalPaymentSystem, PaymentGatewayAdapter


def main():
    print("=== Hotel Reservation System Demo ===")

    # Create customers via factory
    factory = CustomerFactory()
    customer1 = factory.create_customer("John", "Doe", loyalty_status="Premium")
    customer2 = factory.create_customer("Jane", "Smith", loyalty_status="Standard")

    # Show polymorphism in action
    for c in (customer1, customer2):
        print(f"Customer: {c.firstname} {c.lastname}")
        print(f"Rewards message: {c.calculate_rewards()}")

    # Create a reservation and attach observers (Observer pattern)
    reservation = Reservation(
        purpose="Leisure",
        room_type="Double",
        num_rooms=1,
        checkin_date="2024-12-01",
        checkout_date="2024-12-05",
        payment_type="Credit Card",
        customer=customer1,
    )
    reservation.add_observer(EmailObserver())
    reservation.add_observer(SMSObserver())

    # Confirm reservation (will notify observers)
    print(reservation.generate_confirmation())

    # Process a payment using an external gateway via an Adapter
    external_gateway = ExternalPaymentSystem()
    payment_adapter = PaymentGatewayAdapter(external_gateway)
    amount = reservation.total_amount()
    result = payment_adapter.process_payment(amount)
    print(f"Payment processed: {result}")


if __name__ == "__main__":
    main()
