"""Здесь надо написать тесты с использованием pytest для модуля item."""


import pytest

from src.item import Item


@pytest.fixture
def test_item():
    return Item('One', 2, 3)


def test_init(test_item):
    assert test_item.name == 'One'
    test_item.name = 'Three'
    assert test_item.name == 'Three'
    assert test_item.price == 2
    assert test_item.quantity == 3


def test_calculate_total_price(test_item):
    total_price = test_item.calculate_total_price()
    assert total_price == 6
    assert test_item.pay_rate == 1.0
    test_item.pay_rate = 2
    assert test_item.pay_rate == 2


def test_apply_discount(test_item):
    discount = test_item.apply_discount()
    assert discount == 2
    discount_sale = test_item.apply_discount()
    assert discount_sale == 2.0
