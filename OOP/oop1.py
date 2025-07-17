from abc import ABC, abstractmethod
from datetime import datetime, timezone
import json
import os
from typing import TextIO


class Phone(ABC):
    phones_created = 0

    def __init__(self, manufacturer: str, model: str, year_of_release: int, ram: int, memory: int,
                 battery_capacity: int):
        self.manufacturer = manufacturer
        self.model = model
        self.year_of_release = year_of_release
        self.ram = ram
        self.memory = memory
        self.battery_capacity = battery_capacity
        Phone.phones_created += 1

    def _make_data(self):
        return {
            "Производитель": {
                self.manufacturer: {
                    "Модель": self.model,
                    "Год выпуска": self.year_of_release,
                    "Озу": self.ram,
                    "Память": self.memory,
                    "Аккумулятор": self.battery_capacity,
                    "Дата поступления": datetime.now(timezone.utc).astimezone().isoformat()
                }
            }
        }

    @staticmethod
    def _load_json(filename="data.json"):
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    @staticmethod
    def _save_json(data, filename="data.json"):
        # пробовал указать тип, чтобы убрать предупреждение
        """Expected type 'SupportsWrite[str]', got 'TextIO' instead"""
        # в целом работает как надо, но глаз мозолит,
        with open(filename, "w", encoding="utf-8") as file:  # type: TextIO
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def get_total_created(cls):
        return f"Всего телефонов создано: {cls.phones_created}"

    @staticmethod
    # отсебячина , современный телефон или нет
    def is_modern(year: int):
        return int(year) >= 2020

    @abstractmethod
    def create_data(self):
        pass

    @staticmethod
    def get_data(filename="data.json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            print("Есть в наличии:")
            for item in data:
                print(item)

    def delete_data(self, filename="data.json"):
        self._save_json([], filename)
        print("Все данные удалены.")


class Iphone(Phone):
    def create_data(self):
        data = self._load_json()
        data.append(self._make_data())
        self._save_json(data)
        print(f"{self.model} добавлен в базу данных")


class Android(Phone):
    def create_data(self):
        data = self._load_json()
        data.append(self._make_data())
        self._save_json(data)
        print(f"{self.model} добавлен в базу данных")


class Iphone15(Iphone):
    def __init__(self, year, ram, memory, battery_capacity, serial_number):
        super().__init__("Apple", "iPhone 15", year, ram, memory, battery_capacity)
        self._serial_number = serial_number

    def dynamic_island(self):
        print(f"{self.model} использует Dynamic Island")

    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        if not value or len(value) < 5:
            raise ValueError("Серийный номер должен быть не короче 5 символов")
        self._serial_number = value


class Iphone4(Iphone):
    def __init__(self, year, ram, memory, battery_capacity):
        super().__init__("Apple", "iPhone 4", year, ram, memory, battery_capacity)

    def legacy_port(self):
        print(f"{self.model} использует старый 30-pin разъём")


"""
iphone15 = Iphone15(2023, 6, 256, 4000, "SN12345")
iphone15.create_data()
print("Серийник:", iphone15.serial_number)
iphone15.serial_number = "NEW67890"  # setter
print("Новый серийник:", iphone15.serial_number)

print(Phone.get_total_created())  # classmethod
print("Современный?", Phone.is_modern(iphone15.year_of_release))  # staticmethod

Xiaomi13 = Android("Xiaomi LLC", "Xiaomi 13", 2022, 8, 256, 4500)
Xiaomi13.create_data()"""