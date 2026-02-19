from pathlib import Path

import pytest

from src.main import Category, Product, load_data_from_json


@pytest.fixture
def sample_products() -> list[Product]:
    return [Product("Test1", "Desc1", 100.0, 5), Product("Test2", "Desc2", 200.0, 3)]


def test_product_initialization() -> None:
    product = Product("Phone", "Smartphone", 99999.99, 10)
    assert product.name == "Phone"
    assert product.description == "Smartphone"
    assert product.price == 99999.99
    assert product.quantity == 10


def test_category_initialization(sample_products: list[Product]) -> None:
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Electronics", "Devices", sample_products)
    assert category.name == "Electronics"
    assert category.description == "Devices"
    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_multiple_categories() -> None:
    Category.category_count = 0
    Category.product_count = 0

    products1 = [Product("P1", "D1", 10.0, 1)]
    products2 = [Product("P2", "D2", 20.0, 2), Product("P3", "D3", 30.0, 3)]

    Category("Cat1", "Desc1", products1)
    Category("Cat2", "Desc2", products2)

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_load_from_json() -> None:
    Category.category_count = 0
    Category.product_count = 0

    # путь к JSON в корне проекта
    file_path = Path(__file__).resolve().parent.parent / "products.json"
    categories = load_data_from_json(file_path)

    assert len(categories) == 2
    assert Category.category_count == 2
    assert Category.product_count == 4
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 3
