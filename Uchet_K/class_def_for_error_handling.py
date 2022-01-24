import ctypes
import time


class false_in_file_zapis_uchet_k(Exception):
    """
    Создание класса для обработки ошибок в текстовом файле Zapis_uchet_k.txt
    """
    pass


class false_in_file_abonenti(Exception):
    """
    Создание класса для обработки ошибок в текстовом файле Abonenti.txt
    """
    pass


class diapozon_value_error(Exception):
    """
    Создание класса для обработки ошибок в текстовом файле Abonenti.txt,
    если значение 2 аргумента в строке не попадает в диапозон от
    1 до 14, то есть возможных типов абонентов
    """
    pass


def notification(title, text):
    """
    Функция вывода уведомления, принимает заголовок и текст
    """
    return ctypes.windll.user32.MessageBoxW(0, text, title, 0)


def check_date(date, iteration_number):
    """
    Функция провеки параметра даты в файле Zapis_uchet_k.txt, принимает дату
    и номер итерации в цикле для вывода уведомления
    """
    try:
        valid_date = time.strptime(date, '%d.%m.%Y')
    except ValueError:
        notification("Ошибка в текстовом файле Zapis_uchet_k.txt",
                     "Проверьте значение даты в строке " + str(
                         iteration_number) + "!")
        exit()


def check_time(time_value, iteration_number):
    """
    Функция провеки параметра времени в файле Zapis_uchet_k.txt, принимает значение
    и номер итерации в цикле для вывода уведомления
    """
    try:
        valid_time = time.strptime(time_value, '%H:%M')
    except ValueError:
        notification("Ошибка в текстовом файле Zapis_uchet_k.txt",
                     "Проверьте значение времени в строке " + str(
                         iteration_number) + "!")
        exit()


def check_user(seans_user_id_abonent):
    """
    Функция провеки соответствия пользователя в файле Zapis_uchet_k.txt со списком пользователей в файле
    Abonenti.txt, принимает значение и номер итерации в цикле для вывода уведомления
    """
    if seans_user_id_abonent == None:
        try:
            raise diapozon_value_error()
        except diapozon_value_error:
            notification("Ошибка соответствия",
                         "Проверьте значение пользователя в файлах Zapis_uchet_k.txt и Abonenti.txt!")
            exit()
