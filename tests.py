from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # #нет такого словаря, он переименован  в genre
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_duplicate_book(self):
            collector = BooksCollector()

            collector.add_new_book('Гордость и предубеждение и зомби')
            count_before = len(collector.get_books_genre())

            collector.add_new_book('Гордость и предубеждение и зомби')

            assert len(collector.get_books_genre()) == count_before


    def test_set_book_genre_check_genre_detection(self):
        collector = BooksCollector()

        collector.add_new_book("Приключения Шерлока Холмса")
        collector.set_book_genre("Приключения Шерлока Холмса", "Детективы")
        assert collector.get_book_genre("Приключения Шерлока Холмса") == "Детективы"

    def test_set_book_genre_check_invalid_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Хроники Нарнии")
        collector.set_book_genre("Хроники Нарнии", "Фентези")
        assert collector.get_book_genre("Хроники Нарнии") == ""

    def test_get_books_with_specific_genre_simple_genres(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Что делать, если ваш кот хочет вас убить']

    def test_get_books_genre_empty(self):
        collector = BooksCollector()

        assert collector.get_books_genre() == {}

    def test_get_list_of_favorites_books_with_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Хроники Нарнии')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Хроники Нарнии')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Хроники Нарнии']

    def test_get_books_for_children_one_unsuitable_book_(self):
        collector = BooksCollector()

        collector.add_new_book('Хроники Нарнии')
        collector.set_book_genre('Хроники Нарнии', 'Фантастика')
        collector.add_new_book('Зомбиленд')
        collector.set_book_genre('Зомбиленд', 'Ужасы')
        collector.add_new_book('Свинка Пеппа')
        collector.set_book_genre('Свинка Пеппа', 'Комедии')

        assert collector.get_books_for_children() == ['Хроники Нарнии', 'Свинка Пеппа']

    def test_add_book_in_favorites_duplicate_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        count_before = len(collector.get_list_of_favorites_books())


        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == count_before

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        # Удаляем Книга 1 из Избранного
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()
