from hotel.customer import StandardCustomer, PremiumCustomer


def test_polymorphic_rewards_messages():
    std = StandardCustomer("Alice", "Brown")
    prem = PremiumCustomer("Bob", "Green", rewards_points=150)

    msg_std = std.calculate_rewards()
    msg_prem = prem.calculate_rewards()

    assert "Standard rewards" in msg_std
    assert "Premium rewards" in msg_prem
    assert "150" in msg_prem
