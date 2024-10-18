"""
OOP. Classes and inheritance, super, magic methods, etc.

Основные принципы ООП включают инкапсуляцию, наследование, полиморфизм и абстракцию. 
Инкапсуляция скрывает внутренние детали реализации и защищает данные, предоставляя доступ через методы. 
Наследование позволяет создавать новые классы на основе существующих, а полиморфизм позволяет использовать один и тот же интерфейс для объектов разных классов. 
Абстракция упрощает сложные системы, скрывая ненужные детали и выделяя ключевые характеристики.

OOPs Concepts in Python
Class in Python
Objects in Python
Polymorphism in Python
Encapsulation in Python
Inheritance in Python
Data Abstraction in Python

"""
import typing


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
    print(QWE.mro())
    print(dir(QWE))
