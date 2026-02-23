from src.main import Category, Product


def test_product_str() -> None:
    product = Product("Test", "Desc", 100.0, 5)
    assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."


def test_category_str() -> None:
    p1 = Product("A", "Desc", 100.0, 5)
    p2 = Product("B", "Desc", 200.0, 3)
    category = Category("Tech", "Desc", [p1, p2])

    assert str(category) == "Tech, количество продуктов: 8 шт."


def test_product_add() -> None:
    p1 = Product("A", "Desc", 100.0, 5)
    p2 = Product("B", "Desc", 200.0, 2)

    assert p1 + p2 == 100 * 5 + 200 * 2


def test_category_iteration() -> None:
    p1 = Product("A", "Desc", 100.0, 5)
    p2 = Product("B", "Desc", 200.0, 3)
    category = Category("Tech", "Desc", [p1, p2])

    products = [product for product in category]

    assert products == [p1, p2]
