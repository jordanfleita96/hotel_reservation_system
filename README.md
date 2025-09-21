# Hotel Reservation System (OOP + Design Patterns)

A minimal Python project demonstrating OOP (encapsulation, inheritance, polymorphism, abstraction)
and design patterns (Factory, Observer, Adapter) via a hotel reservation example.

## Features
- Customers: Standard vs Premium with polymorphic `calculate_rewards()`
- Observer notifications (Email/SMS) when a reservation is confirmed
- Factory for customer creation by loyalty status
- Adapter wrapping a mock external payment gateway
- Demo (`main.py`) + tests (`pytest`) + CI (GitHub Actions)

## Requirements
- Python 3.10+
- `pytest` (install via `requirements.txt`)

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
