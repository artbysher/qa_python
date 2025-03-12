# qa_python
# Тестирование класса BooksCollector

Это набор тестов, написанных для класса `BooksCollector`, который позволяет установить жанр книг и добавить их в избранное. 

## Структура тестов

Представленны тесты для проверки некоторых аспектов функциональности класса. Для создания экземпляр класса `BooksCollector` используется фикстура collector для каждого теста.

Тесты

*-* 1. Тестирование добавления новой книги

- *Тест*: `test_add_new_book_add_two_books`
    - *Описание*: Проверяет, что две книги добавлены в коллекцию.
    - *Ожидаемый результат*: Длина словаря жанров должна быть равна 2.

*-*  2. Проверка добавления дубликата книги

- *Тест*: `test_add_new_book_add_duplicate_book`
    - *Описание*: Проверяет, что повторная попытка добавления уже существующей книги не увеличивает количество книг в коллекции.
    - *Ожидаемый результат*: Длина словаря жанров должна оставаться прежней.

*-*  3. Установка и получение жанра книги 

- *Тест*: `test_set_book_genre_check_genre_detection`
    - *Описание*: Проверяет возможность установки жанра книги и его корректное извлечение.
    - *Ожидаемый результат*: Жанр книги должен совпадать с установленным.

*-*  4. Проверка установки несуществующего жанра 

- *Тест*: `test_set_book_genre_check_invalid_genre`
    - *Описание*: Проверяет, что установка жанра, которого нет в списке определенных жанров, игнорируется. С помощью параметризации проводится 5 тестов.
    - *Ожидаемый результат*: Жанр книги должен оставаться пустым как и до установки жанра не определенного в списке..

*-* 5. Получение текущего словаря books_genre без жанров

- *Тест*: `test_get_book_genre_dictionary_when_two_books`
    - *Описание*: Проверяет, что метод возвращает список книг.
    - *Ожидаемый результат*: Должен возвращаться словарь с переданными названиями книг и с пустым значением жанра.

*-* 5.1. Получение книг определенного жанра

- *Тест*: `test_get_books_with_specific_genre_simple_genres`
    - *Описание*: Проверяет, что метод возвращает список книг с заданным жанром.
    - *Ожидаемый результат*: Должен возвращаться список книг, соответствующий запросу.

*-* 6. Получение пустого словаря books_genre

- *Тест*: `test_get_books_genre_empty_dictionary_when_no_books`
    - *Описание*: Проверяет, что если не было добавленно ни оной книги вернется  - пустой словарь.
    - *Ожидаемый результат*: Метод должен возвращать пустой словарь.

*-* 7. Проверяем возврат неустановленного жанра 

- *Тест*: `test_get_book_genre_returns_empty_for_unset_genre`
    - *Описание*: Проверяет, что если была добавлена книга без жанра вернется  - пустая строка.
    - *Ожидаемый результат*: Метод должен возвращать пустую строку.

*-* 8. Получение книг, подходящих детям

- *Тест*: `test_get_books_for_children_one_unsuitable_book_`
    - *Описание*: Проверяет, что метод возвращает только книги, подходящие для детей.
    - *Ожидаемый результат*: Список должен содержать только безопасные для детей книги и не включать книги с жанрами 'Ужасы'и 'Детективы'.

*-* 9. Проверка невозможности добавить книгу повторно в список Ибранных книг

- *Тест*: `test_add_book_in_favorites_duplicate_in_favorites`
    - *Описание*: Проверяет, что повторное добавление книги в избранное не увеличивает количество книг в избранном.
    - *Ожидаемый результат*: Длина списка избранных книг должна оставаться прежней.

*-* 10. Удаление книги из избранного

- *Тест*: `test_delete_book_from_favorites`
    - *Описание*: Проверяет, что книга правильно удаляется из избранного.
    - *Ожидаемый результат*: Книга не должна находиться в списке избранных книг после удаления.

*-* 11. Получение списка Избранных книг

- *Тест*: `test_get_list_of_favorites_books_with_books`
    - *Описание*: Проверяет, что список избранных книг правильно возвращает добавленные книги.
    - *Ожидаемый результат*: Должен возвращаться список избранных книг.

*-* 12. Получение пустого списка Избранных книг

- *Тест*: `test_get_list_of_favorites_books_returns_empty_list_when_no_books`
    - *Описание*: Проверяет, что если книги не добавлялись в список Избранных книг возвращает пустой список.
    - *Ожидаемый результат*: Должен возвращаться пустой список.

Тесты проходят без ошибок, подтверждая корректность поведения класса `BooksCollector`.

