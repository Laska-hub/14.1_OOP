from src.main import Category, Product


def test_add_product() -> None:
    product = Product("Test", "Desc", 100.0, 5)
    category = Category("Cat", "Desc", [])
    category.add_product(product)

    assert "Test" in category.products


def test_new_product_duplicate() -> None:
    product1 = Product("Phone", "Desc", 100.0, 5)
    products = [product1]

    new_data = {
        "name": "Phone",
        "description": "Desc",
        "price": 200.0,
        "quantity": 3,
    }

    result = Product.new_product(new_data, products)

    assert result.quantity == 8
    assert result.price == 200.0


def test_price_setter_invalid() -> None:
    product = Product("Test", "Desc", 100.0, 5)
    product.price = -10

    assert product.price == 100.0
