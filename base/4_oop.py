"""
OOP. Classes and inheritance, super, magic methods, etc.

Основные принципы ООП включают инкапсуляцию, наследование, полиморфизм и абстракцию. 

OOPs Concepts in Python

Class in Python

В Python класс — это шаблон или чертёж для создания объектов. 
Objects in Python - Объекты — это конкретные экземпляры класса, которые могут содержать данные (атрибуты) и функции (методы), связанные с этими данными

Polymorphism in Python - полиморфизм позволяет использовать один и тот же интерфейс для объектов разных классов. что смысл
                         операции зависит от обрабатываемых ею объектов.
Encapsulation in Python - Инкапсуляция скрывает внутренние детали реализации и защищает данные, предоставляя доступ через методы
Inheritance in Python - аследование позволяет создавать новые классы на основе существующих
Data Abstraction in Python - Абстракция упрощает сложные системы, скрывая ненужные детали и выделяя ключевые характеристики.


What is a class
What is "self" - self в Python — это ссылка на текущий экземпляр класса. указатель на текущий объект. 
What __dict__ attribute means -  __dict__ представляет собой словарь, который хранит все атрибуты и их значения для конкретного экземпляра класса
How to declare a class
How to inherit from a class - существует Single и множественное наследование, Класс может наследоваться от нескольких классов, то Пайтон будет использовать: 





Difference between class and an instance of it
"""
import typing

"""
# Classes are defined in CamelCase How to declare a class
# class ClassName: 
#    <body>
# _protected - Защищённые атрибуты предназначены для внутреннего использования в классе и его подклассах, но не скрываются как приватные.
# __private - В Python нет настоящих приватных переменных, поэтому манглирование имён — это способ предотвратить случайный доступ или изменение атрибута извне класса или в подклассах.

# Даже если у нас и есть возможность устанавливать аттрибуты класса в теле класса, __init__

# How to inherit from a class - 
"""
# Parent class
class Animal:
    def speak(self):
        return "Animal sound"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"


"""
Множественное наследование
# MRO — Method Resolution Order) для определения, какой метод будет вызван. Вы можете узнать порядок разрешения методов, используя атрибут __mro__ или метод mro() для любого класса:
"""
class A:

    class_attrs = None

    def __init__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        self.__test_arg = None

    def __len__(self) -> int:
        return len(self.args) + len(self.kwargs)

    def __bool__(self) -> bool:
        return bool(self.__test_arg)

    def main(self) -> None:
        print('Вызов внутри: A')

    @property
    def test_arg(self) -> typing.Any:
        return self.__test_arg

    @test_arg.setter
    def test_arg(self, value: typing.Any):
        self.__test_arg = value


class B(A):

    def main(self) -> None:
        print('Вызов внутри: B до super')
        super().main()
        print('Вызов внутри: B после super')

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)

    @staticmethod
    def get_test() -> str:
        return 'test'


class C(B):

    def main(self) -> None:
        print('Вызов внутри: C до super')
        super().main()
        print('Вызов внутри: C после super')


class D(A):

    def main(self) -> None:
        print('Вызов внутри: D до super')
        super().main()
        print('Вызов внутри: D после super')


class QWE(C, D):

    def main(self) -> None:
        print('Вызов внутри: QWE до super')
        super().main()
        print('Вызов внутри: QWE после super')


if __name__ == '__main__':
    qwe = QWE()
    qwe.main()
    print(QWE.__mro__())
    print(dir(QWE))
