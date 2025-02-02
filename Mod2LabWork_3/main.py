import doctest

class Book:
    """
            Создание базового объекта в виде литературного произведения

            :param name: Название произведения
            :param author: Автор произведения

            Примеры:
            >>> book1 = Book("Капитанская дочка", "А.С. Пушкин")
            >>> print(book1)
    """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    """ Использование __str__ и __repr__ нужно для корректного вывода информации в консоль """

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    """ 2 элемента с @property действуют так, чтобы переменные name и author были доступны только для чтения """

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

class PaperBook(Book):
    """
            Создание объекта в виде бумажного литературного произведения с капелькой наследования из базового класса Book

            :param pages: Количество страниц в книге

            Примеры:
            >>> book1 = Book("Капитанская дочка", "А.С. Пушкин")
            >>> paperbook1 = PaperBook(book1.name,book1.author,500)  # инициализация экземпляра класса
            >>> print(paperbook1) # вывод данных
    """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    """ 2 элемента с @property и @pages.setter действуют так, чтобы переменная pages былa доступна только для чтения """

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        """ Валидация количества страниц и выдача ошибки """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self._pages = value

    def __str__(self):
        return f"Бумажная {super().__str__()}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

class AudioBook(Book):
    """
            Создание объекта в виде бумажного литературного произведения с капелькой наследования из базового класса Book

            :param duration: Длительность аудиокниги в минутах

            Примеры:
            >>> book1 = Book("Капитанская дочка", "А.С. Пушкин")
            >>> audiobook1 = AudioBook(book1.name,book1.author,190.54)  # инициализация экземпляра класса
            >>> print(audiobook1) # вывод данных
    """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    """ 2 элемента с @property и @pages.setter действуют так, чтобы переменная duration былa доступна только для чтения """

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        """ Валидация длительности аудиокниги и выдача ошибки """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self):
        return f"Аудио{super().__str__()}. Продолжительность: {self.duration} Минут"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

if __name__ == "__main__":
    doctest.testmod()