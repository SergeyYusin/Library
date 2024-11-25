class Library:
    def __init__(self):
        self.id = 0
        self.title = None
        self.author = None
        self.year = None
        self.status = 'В наличии'
        self.data = {}

    """ 
        1. Метод 'record' принимает 3 параметра {название книги - title}, {Автора - author} и {год издания - year}  
    """

    def record(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year
        if self.title or self.author or self.year:  # проверяем вхождение одного из параметров если True, ID +1
            self.id += 1
        with open('output.txt', 'w', encoding='utf-8') as file:  # открываем .txt файл для записи
            self.data[self.id] = {'title': self.title,
                                  'author': self.author,
                                  'year': self.year,
                                  'status': self.status}  # записываем данные книги в словарь с новым ID
            for recording in self.data.items():
                file.write(str(recording) + '\n')
            file.close()
        print(f'ID {self.id}:'
              f' Книга "{self.title}",'
              f' Автор "{self.author}",'
              f' "{self.year} года",'
              f' добавлена в библиотеку.')

    """
        2. Метод 'delete' принимает id книги {delete_id} 
    """

    def delete(self, delete_id: int):
        if delete_id in self.data.keys():  # если есть ID в словаре
            print(f'ID {delete_id}:'
                  f' Книга "{self.data[delete_id]['title']}",'
                  f' Автор "{self.data[delete_id]['author']}",'
                  f' "{self.data[delete_id]['year']} года",'
                  f' удалена из библиотеки.')

            del self.data[delete_id]  # удалить запись из словаря
            with open('output.txt', 'w', encoding='utf-8') as file:
                for recording in self.data.items():
                    file.write(str(recording) + '\n')  # записываем новую запись после удаления
                file.close()

        else:
            print('Книга не найдена в библиотеке.')

    """
        3. Метод 'search' принимает title, author или year
    """

    def search(self, title_author_year: str):
        print(f'Поиск книг по заголовку, автору или году издания: {title_author_year}')

        if title_author_year:  # если переменная существует,
            # проверяем все значения словаря на наличие вхождения в переданной переменной,
            # ищем в словаре совпадения и приводим строку к нижнему регистр.
            found_books = [book for book in self.data.values()  # записываем в переменную found_books найденную книгу
                           if title_author_year in book.values()]
            if found_books:                 # если нашли совпадения
                print('Найденные книги:')
                for book in found_books:  # проходим по созданной переменной циклом for и выводим результат поиска по ключу
                    print(
                        f'ID {list(self.data.keys())[list(self.data.values()).index(book)]}'
                        f' | Книга: {book["title"]}, '
                        f'Автор: {book["author"]}, '
                        f'год издания: {book["year"]}')
            else:
                print('Книга не найдена.')
        else:
            print('Вы не ввели ни одного параметра поиска.')

        '''
    #  5. changing_the_status - Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).
        '''

    def changing_the_status(self, id: int, status: str):
        if id in self.data.keys():                    # если есть ID изменить статус по ключу на статус который написали
            self.data[id]['status'] = status
            with open('output.txt', 'w', encoding='utf-8') as file:
                for recording in self.data.items():
                    file.write(str(recording) + '\n')           # записали изменения в .txt
                file.close()
            print(f'Статус книги "{self.data[id]["title"]}" изменен: {status.capitalize()}')
        else:
            print('Книга не найдена в библиотеке.')


    '''
      4. Отображение всех книг в библиотеке: Программа выводит список всех книг в библиотеке с их ID, заголовком, автором, годом издания и статусом.
    '''

    def call(self):
        if not self.data:           # если словарь пуст пишем "Библиотека пуста."
            print('Библиотека пуста.')
        else:
            for key, value in self.data.items():        # если есть значения выдает результат всех книг
                print(f'ID {key} | '
                      f'Книга: {str(self.data[key]['title'])}, '
                      f'Автор: {str(self.data[key]['author'])}, '
                      f'Год издания: {str(self.data[key]['year'])}, '
                      f'Статус : {str(self.data[key]['status']).capitalize()}')

    '''
    Функция main запускает программу 
    '''


def main() -> None:
    print('Приветствуем вас в библиотеке!')
    library = Library()
    while True:                                 # запуск программы
        main = input('Выберите действия\n'
                     '"1" - Добавление книги:\n'
                     '"2" - Удаление книги по ID:\n'
                     '"3" - Поиск книги:\n'
                     '"4" - Отображение всех книг:\n'
                     '"5" - Изменение статуса книги по ID:\n'
                     '"0" - Остановить программу:\nВвод - ')
        while not main.isdigit():                        # пока не введут число спрашивать
            print('\t"Неправильный ввод, введите цифру"')
            main = input('Выберите действия\n'
                         '"1" - Добавление книги:\n'
                         '"2" - Удаление книги по ID:\n'
                         '"3" - Поиск книги:\n'
                         '"4" - Отображение всех книг:\n'
                         '"5" - Изменение статуса книги по ID:\n'
                         '"0" - Остановить программу:\nВвод - ')

        if int(main) == 1:                                  # запись книги
            title = input('Введите название книги: ')
            while not title:                                # пока не ввели спрашивать
                title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            while not author:                                # пока не ввели спрашивать
                author = input('Введите автора книги: ')
            year = input('Введите год издания: ')
            while not year:                                 # пока не ввели спрашивать
                year = input('Введите год издания: ')
            while not year.isdigit():                       # пока не число повторить запрос
                year = input('Введите год издания (только цифры): ')
            library.record(title.capitalize(), author.capitalize(), year)    # отправка в данных в класс "Library" метод "record"

        elif int(main) == 2:                                # удалить книгу
            delete_id = input('Введите ID книги для удаления: ')
            while not delete_id.isdigit():                  # пока не число спрашивать ID
                delete_id = input('Неправильный ввод ID книги, для удаления напишите ID цифрой без пробелов: ')
            library.delete(int(delete_id))                  # отправка в данных в класс "Library" метод "delete"

        elif int(main) == 3:                                # поиск книги
            title_author_year = input('Введите название, автора или год издания книги: ')
            library.search(title_author_year.capitalize())               # отправка в данных в класс "Library" метод "search"

        elif int(main) == 4:                                # вывести всю библиотеку
            library.call()                                  # отправка в данных в класс "Library" метод "call"

        elif int(main) == 5:                                # изменение статуса
            id_status = input('Введите ID книги для изменения статуса: ')
            while not id_status.isdigit():                  # если не число повторить запрос
                id_status = input('Неправильный ввод ID книги, для изменения статуса напишите ID цифрой: ')
            status = input('Введите новый статус (в наличии или выдана): ')
            while status.lower() not in ['в наличии', 'выдана']:        # проверка на корректность ввода и запрашивает повторный запрос
                status = input('Неправильный ввод статуса, введите "в наличии" или "выдана": ')
            library.changing_the_status(int(id_status), status)         # отправка в данных в класс "Library" метод "changing_the_status"
        elif int(main) == 0:                                # остановка программы
            print('Программа завершена.')
            break
        else:                                               # если в запуске не правильно ввели запрос выводить уведомление
            print('\t"Неправильный ввод, попробуйте снова"')


# Запуск программы
if __name__ == '__main__':
    main()
