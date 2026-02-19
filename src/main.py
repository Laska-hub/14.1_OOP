import json
from pathlib import Path
from typing import List


class Product:
    """Класс товара"""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity


class Category:
    """Класс категории товаров"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name: str = name
        self.description: str = description
        self.products: List[Product] = products

        Category.category_count += 1
        Category.product_count += len(products)


def load_data_from_json(file_path: str | Path) -> List[Category]:
    """Загружает данные из JSON и создаёт объекты Category и Product"""
    categories: List[Category] = []
    file_path = Path(file_path)

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

        for category_data in data:
            products: List[Product] = []
            for product_data in category_data["products"]:
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
                products.append(product)

            category = Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
            categories.append(category)

    return categories


if __name__ == "__main__":
    # Пути к JSON
    BASE_DIR = Path(__file__).resolve().parent.parent  # поднимаемся в корень
    json_file = BASE_DIR / "products.json"

    # Загрузка из JSON
    categories = load_data_from_json(json_file)

    print("После загрузки JSON:")
    for cat in categories:
        print(cat.name)
        print(cat.description)
        print("Количество товаров:", len(cat.products))

    print("Всего категорий:", Category.category_count)
    print("Всего товаров:", Category.product_count)
