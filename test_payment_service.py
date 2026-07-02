from payment_service import PaymentService
import pytest


def test_calculate_tax():
    service = PaymentService()
    assert service.calculate_total(100) == 118


def test_negative_amount():
    service = PaymentService()

    with pytest.raises(ValueError):
        service.calculate_total(-100)


def test_daily_limit():
    service = PaymentService()

    with pytest.raises(ValueError):
        service.process_payment(15000)