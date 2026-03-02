import pytest

from src.main import BaseProduct, Category, LawnGrass, Product, Smartphone


def test_product_str() -> None:
    product = Product("Test", "Desc", 100.0, 5)
    assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."


def test_product_add_same_type() -> None:
    p1 = Product("A", "Desc", 100.0, 5)
    p2 = Product("B", "Desc", 200.0, 2)

    assert p1 + p2 == 100 * 5 + 200 * 2


def test_product_add_different_type() -> None:
    p1 = Product("A", "Desc", 100.0, 5)
    s1 = Smartphone("Phone", "Desc", 100.0, 5, 95.5, "S1", 256, "Black")

    with pytest.raises(TypeError):
        _ = p1 + s1


def test_price_setter_validation() -> None:
    product = Product("Test", "Desc", 100.0, 5)

    with pytest.raises(ValueError):
        product.price = -10


def test_smartphone_inheritance() -> None:
    smartphone = Smartphone(
        "Phone",
        "Desc",
        100.0,
        5,
        95.5,
        "S1",
        256,
        "Black",
    )

    assert isinstance(smartphone, Product)
    assert isinstance(smartphone, BaseProduct)


def test_category_add_product() -> None:
    product = Product("Test", "Desc", 100.0, 5)
    category = Category("Tech", "Desc", [product])

    new_product = Product("New", "Desc", 50.0, 2)
    category.add_product(new_product)

    assert "New" in category.products


def test_category_add_invalid() -> None:
    product = Product("Test", "Desc", 100.0, 5)
    category = Category("Tech", "Desc", [product])

    with pytest.raises(TypeError):
        category.add_product("Not a product")  # type: ignore


def test_lawngrass_creation() -> None:
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
    assert isinstance(grass, Product)
