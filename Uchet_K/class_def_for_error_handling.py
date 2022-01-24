import ctypes
import time


class False_in_file_zapis_uchet_k(Exception):
    """
    Создание класса для обработки ошибок в текстовом файле Zapis_uchet_k.txt
    """
    pass


class False_in_file_abonenti(Exception):
    """
    Создание класса для обработки ошибок в текстовом файле Abonenti.txt
    """
    pass


class Diapozon_value_error(Exception):
    """
    Создание класса для обработки ошибок в текстовом файле Abonenti.txt,
    если значение 2 аргумента в строке не попадает в диапозон от
    1 до 14, то есть возможных типов абонентов
    """
    pass


class False_in_video_com_type(Exception):
    """
    Создание класса для обработки ошибок переменной video_com_type класса Zapis_uchet_k
    """
    pass


class False_in_video_place_id(Exception):
    """
    Создание класса для обработки ошибок переменной video_place_id класса Zapis_uchet_k
    """
    pass


class False_in_dislocation(Exception):
    """
    Создание класса для обработки ошибок переменной dislocation класса Zapis_uchet_k
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
        time.strptime(date, '%d.%m.%Y')
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
        time.strptime(time_value, '%H:%M')
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
            raise Diapozon_value_error()
        except Diapozon_value_error:
            notification("Ошибка соответствия",
                         "Проверьте значение пользователя в файлах Zapis_uchet_k.txt и Abonenti.txt!")
            exit()


def check_video_com_type(video_com_type):
    """
    Функция проверки переменной video_com_type класса Zapis_uchet_k
    """
    try:
        if int(video_com_type) not in range(1, 4):
            raise False_in_video_com_type()
        a = int(video_com_type)
    except False_in_video_com_type:
        notification("Ошибка в текстовом файле Zapis_uchet_k.txt",
                     "Проверьте значение типа сеанса в файле Zapis_uchet_k.txt! Оно должно быть в диапазоне от 1 до 3! 1 - ЗВС, 2 - КВС, 3 - ЗВС+КВС!")
        exit()
    except ValueError:
        notification("Ошибка в текстовом файле Zapis_uchet_k.txt",
                     "Проверьте значение типа сеанса в файле Zapis_uchet_k.txt! Оно должно быть в диапазоне от 1 до 3! 1 - ЗВС, 2 - КВС, 3 - ЗВС+КВС!")
        exit()


def check_video_place_id(video_video_place_id):
    """
    Функция проверки переменной video_video_place_id класса Zapis_uchet_k
    """
    try:
        if int(video_video_place_id) not in [1, 2, 10]:
            raise False_in_video_place_id()
        a = int(video_video_place_id)
    except False_in_video_place_id:
        notification("Ошибка в текстовом файле Zapis_uchet_k.txt",
                     "Проверьте значение студии проведения в файле Zapis_uchet_k.txt! Оно должно быть принадлежать множеству [1, 2, 10]!"
                     " 1 - студия *****, 2 - СЦ *****, 10 - ГФИ *****!")
        exit()
    except ValueError:
        notification("Ошибка в текстовом файле Zapis_uchet_k.txt",
                     "Проверьте значение студии проведения в файле Zapis_uchet_k.txt! Оно должно быть принадлежать множеству [1, 2, 10]!"
                     " 1 - студия *****, 2 - СЦ *****, 10 - ГФИ *****!")
        exit()


def check_dislocation(dislocation):
    """
    Функция проверки переменной dislocation класса Zapis_uchet_k
    """
    try:
        if int(dislocation) not in range(1, 4):
            raise False_in_dislocation()
        a = int(dislocation)
    except False_in_dislocation:
        notification("Ошибка в текстовом файле Zapis_uchet_k.txt",
                     "Проверьте значение дислокации в файле Zapis_uchet_k.txt! Оно должно быть в диапазоне от 1 до 3!"
                     " 1 - Си*****+Се*****, 2 - Си*****, 3 - Се*****!")
        exit()
    except ValueError:
        notification("Ошибка в текстовом файле Zapis_uchet_k.txt",
                     "Проверьте значение дислокации в файле Zapis_uchet_k.txt! Оно должно быть в диапазоне от 1 до 3!"
                     " 1 - Си*****+Се*****, 2 - Си*****, 3 - Се*****!")
        exit()
