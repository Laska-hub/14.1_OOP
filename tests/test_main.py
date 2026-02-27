import pytest
from typing import cast

from src.main import Category, LawnGrass, Product, Smartphone


def test_product_str() -> None:
    product = Product("Test", "Desc", 100.0, 5)
    assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."


def test_category_str() -> None:
    p1 = Product("A", "Desc", 100.0, 5)
    p2 = Product("B", "Desc", 200.0, 3)
    category = Category("Tech", "Desc", [p1, p2])

    assert str(category) == "Tech, количество продуктов: 8 шт."


def test_product_add_same_type() -> None:
    p1 = Product("A", "Desc", 100.0, 5)
    p2 = Product("B", "Desc", 200.0, 2)

    assert p1 + p2 == 100 * 5 + 200 * 2


def test_category_iteration() -> None:
    p1 = Product("A", "Desc", 100.0, 5)
    p2 = Product("B", "Desc", 200.0, 3)
    category = Category("Tech", "Desc", [p1, p2])

    products = [product for product in category]

    assert products == [p1, p2]


# =========================
# 16.1 — Inheritance tests
# =========================


def test_smartphone_creation() -> None:
    phone = Smartphone(
        "Phone",
        "Desc",
        1000.0,
        5,
        95.5,
        "X",
        256,
        "Black",
    )

    assert phone.model == "X"
    assert phone.memory == 256
    assert phone.efficiency == 95.5
    assert isinstance(phone, Product)


def test_lawn_grass_creation() -> None:
    grass = LawnGrass(
        "Grass",
        "Desc",
        500.0,
        10,
        "Russia",
        "7 days",
        "Green",
    )

    assert grass.country == "Russia"
    assert grass.germination_period == "7 days"
    assert isinstance(grass, Product)


def test_add_same_class_products() -> None:
    phone1 = Smartphone(
        "Phone1",
        "Desc",
        100.0,
        5,
        90.0,
        "A",
        128,
        "Black",
    )
    phone2 = Smartphone(
        "Phone2",
        "Desc",
        200.0,
        2,
        92.0,
        "B",
        256,
        "White",
    )

    assert phone1 + phone2 == 100 * 5 + 200 * 2


def test_add_different_class_products() -> None:
    phone = Smartphone(
        "Phone",
        "Desc",
        100.0,
        5,
        90.0,
        "A",
        128,
        "Black",
    )
    grass = LawnGrass(
        "Grass",
        "Desc",
        500.0,
        10,
        "Russia",
        "7 days",
        "Green",
    )

    with pytest.raises(TypeError):
        _ = phone + grass


def test_add_invalid_product_to_category() -> None:
    category = Category("Test", "Desc", [])

    with pytest.raises(TypeError):
        category.add_product(cast(Product, "not a product"))
