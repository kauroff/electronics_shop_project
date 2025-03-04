import csv
import os.path


class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.__name}\', {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        """
        Метод срабатывает, когда используется оператор сложения.
        В параметре other хранится то, что справа от знака +
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError('Сложение возможно только между экземплярами Item или наследниками.')

    @property
    def name(self) -> any:
        return self.__name

    @name.setter
    def name(self, name):
        """Метод срабатывает при операции присваивания."""
        if len(name) < 11:
            self.__name = name
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине. Без учета скидки.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.price * self.pay_rate)

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        if os.path.exists(csv_file):
            with open(csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if len(row) == 3:
                        Item.all.append(Item(row['name'], row['price'], row['quantity']))
                    else:
                        raise InstantiateCSVError
        else:
            raise FileNotFoundError(f'Отсутствует файл {csv_file}')

    @staticmethod
    def string_to_number(string):
        return int(float(string))
