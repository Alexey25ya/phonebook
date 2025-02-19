from colorama import *
import emoji as e
import check as ch


def phone_menu(number: str = '') -> int:
    '''
    Вывод в консоль меню телефонной книги. В возврате запускает модуль, где функция принимает число от пользователя, проверяет и возвращает его.
    '''
    print(e.emojize(
        f'{Style.BRIGHT + Fore.GREEN}Добро пожаловать!:raising_hands:{Style.RESET_ALL}'))
    print(e.emojize(f'{Style.BRIGHT + Fore.YELLOW}Выберите действие с телефонной книгой (введите цифру от 1 до 5): \n{Style.RESET_ALL}'
          '1 - :busts_in_silhouette: Просмотреть все контакты \n'
                    '2 - :eyes: Поиск записи \n'
                    '3 - :writing_hand:  Добавить новый контакт \n'
                    '4 - :spiral_notepad:  Экспорт базы данных в файл \n'
                    '5 - :right_arrow:  Импорт базы данных в телефонную книгу'
                    f'{Style.RESET_ALL}'))
    return ch.check_numbers(number)


def input_search(number: str = '') -> int:
    '''
    Подменю для поиска контакта.
    '''
    print(e.emojize(f'{Style.BRIGHT + Fore.YELLOW}Выберите по какому параметру будет поиск (введите 1 или 2): {Style.RESET_ALL} \n'
                    '1 - :input_latin_lowercase: По имени \n'
                    '2 - :input_numbers: По номеру телефона'))
    return ch.check_numbers(number)


def search_submenu(number: str = '') -> int:
    '''
    Подменю после вызова поиска контакта
    '''
    print(e.emojize(f'{Style.BRIGHT + Fore.YELLOW}:eyes:  Выберите действия для работы: {Style.RESET_ALL} \n'
                    '1 - :broom:  Удалить контакт \n'
                    '2 - :pencil:  Редактировать контакт'))
    return ch.check_numbers(number)


def print_all(data_list: list) -> None:
    '''
    Вывод всех контактов из телефонной книги
    '''
    print(e.emojize(
        f'{Style.BRIGHT + Fore.YELLOW}:busts_in_silhouette:  Ваши контакты: {Style.RESET_ALL}'))
    for line in data_list:
        print(line)


def print_contact(contact_data: str = '') -> None:
    '''
    Выводит определенный контакт в консоль, н-р после поиска, или редактирования, или добавления.
    '''
    print(e.emojize(
        f'{Style.BRIGHT + Fore.YELLOW}:heart_decoration:  Карточка контакта: \n {contact_data}{Style.RESET_ALL}'))


def input_new_contact(new_contact: str = '') -> list:
    '''
    Функция добавляет новые данные, возвращает список строк.
    '''
    contact = []
    print(e.emojize(
        f'{Style.BRIGHT + Fore.YELLOW}:writing_hand:  Добавьте новый контакт: {Style.RESET_ALL}'))
    text = ch.record_length('Имя: ')
    text = text.capitalize()
    contact.append(text)
    text = ch.record_length('Фамилия: ')
    text = text.capitalize()
    contact.append(text)
    text = ch.check_numbers('Номер телефона: ')
    contact.append(text)
    print(e.emojize(
        f'{Style.BRIGHT + Fore.YELLOW}:check_mark_button: Контакт добавлен{Style.RESET_ALL}'))
    return contact


input_new_contact()


def edit_data(contact_data: str = '') -> str:
    '''
    Функция перезаписывает новые данные поверх имеющейся записи
    '''
    print(e.emojize(
        f'{Style.BRIGHT + Fore.YELLOW}:card_index_dividers:  Введите новые данные: {Style.RESET_ALL}'))
    return ch.record_length(contact_data)
