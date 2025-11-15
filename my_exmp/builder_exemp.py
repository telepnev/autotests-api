"""

Что такое паттерн Builder?
Паттерн Builder (Строитель) – это порождающий шаблон проектирования, который используется для пошагового создания сложных объектов. Вместо того чтобы создавать объект сразу с большим количеством аргументов в конструкторе, мы разделяем процесс создания на последовательные шаги.

Основные принципы паттерна Builder:

Отделение процесса создания объекта от его представления – клиентский код не должен заботиться о том, как именно создается объект.
Гибкость в конфигурации – можно динамически задавать параметры объекта, не перегружая конструктор.
Читаемость кода – создание объекта становится интуитивно понятным и структурированным.

"""


class Car:
    # конструктор
    def __init__(self, engine, wheels, color, doors):
        self.engine = engine
        self.wheels = wheels
        self.color = color
        self.doors = doors


class CarBuilder:
    # конструктор с полями по умолчанию
    def __init__(self):
        self.engine = None
        self.wheels = 4
        self.color = "white"
        self.doors = 4

    def set_engine(self, engine):
        self.engine = engine
        return self

    def set_color(self, color):
        self.color = color
        return self

    def set_doors(self, doors):
        self.doors = doors
        return self

    def build(self):
        return Car(self.engine, self.wheels, self.color, self.doors)


# Использование:
builder = CarBuilder()
car = builder.set_engine("V8").set_color("red").build()
super_car = builder.set_engine("V12").set_color("blue").set_doors(2).build()

print(F"car = {car.engine, car.wheels, car.color}")
print(F"super_car = {super_car.engine, super_car.wheels, super_car.color, super_car.doors}")
