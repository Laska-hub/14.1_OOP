from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Iterator, List


class BaseProduct(ABC):
    """Абстрактный базовый класс продукта."""

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта."""

    @abstractmethod
    def __add__(self, other: object) -> float:
        """Сложение продуктов."""


class InitReprMixin:
    """Миксин, выводящий информацию о создании объекта."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(f"{self.__class__.__name__}{args}")
        super().__init__(*args, **kwargs)


class Product(InitReprMixin, BaseProduct):
    """Класс товара."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float:
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")

        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")

        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self.__price = value


class Smartphone(Product):
    """Класс смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс категории товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: List[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: " f"{total_quantity} шт."

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только Product " "или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    def __iter__(self) -> Iterator[Product]:
        return iter(self.__products)
