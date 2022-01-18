"""
------------------------------------------------------------------------------------------------------------
Задача: автоматизовать процесс заполнения учетных записей сеансов в Учет-К
Исполнение: ввиду разделения сетей из соображения безопасности возможности брать данные непостредственно
с сети ***** не представляется возможным, поэтому оператору придется вручную заполнять
файл Zapis_uchet_k.txt с записями по образцу:
ФАМИЛИЯ_АБОНЕНТА ДАТА_СЕАНСА НАЧАЛО_ТЕХНИЧЕСКОГО_СЕАНСА НАЧАЛО_СЕАНСА КОНЕЦ_СЕАНСА
Также в файле Abonenti.txt содержится соответствие абонент:принадлежность для работы программы, перед
запуском обязательно проверьте, есть ли этот абонент в текстовом файле, при необходимости внесите
изменения в файл, при желании в программе можно изменить конечный текстовый файл.
------------------------------------------------------------------------------------------------------------
Version 1.0 17.01.2022 Исполнил: Григорьев Никита Сергеевич
Первая версия программы все реализован в виде функций и классов для масштабируемости кода, подробнее можно
рассмотреть в самом коде, комментарии написаны явно. Из недостатков отмечаю отсутствие обработки ошибок,можно
доработать и возможно аутентификацию стоит делать 1 раз, это повысит скорость выполнения команды.
------------------------------------------------------------------------------------------------------------
"""

import requests
from datetime import datetime
from datetime import timedelta


class zapis_uchet_k:
    """
    Инициализация класса для создания экземпляров записи и метода push в Учет-К
    """

    def __init__(self, user, date, start_tehnicheskogo_session, start_session, finish_session):
        # Атрибуты с которыми будем работать
        self.user = user
        self.date = date
        self.start_tehnicheskogo_session = start_tehnicheskogo_session
        self.start_session = start_session
        self.finish_session = finish_session
        # Атрибуты, которые будем push, с помощью метода, общие
        self.seans_user_id = seans_user_id_init(user)  # тип абонента
        self.video_com_type = '1'  # пока только ЗВС
        self.video_place_id = '1'  # пока по умолчанию ЗВС
        self.podr_id = '1207692237'  # всегда *****
        self.seans_datetime_sel = date  # дата проведения
        self.trud_peoples = '1'  # количество людей всегда 1
        # Атрибуты, которые будем push, с помощью метода, только технического сеанса
        self.video_type_id_technical = '1'  # тип сеанса - технический
        self.seans_time_technical = time_difference(start_tehnicheskogo_session, start_session)[0]
        self.trud_hours_technical = time_difference(start_tehnicheskogo_session, start_session)[1]
        self.comment_simferopol_technical = str(start_tehnicheskogo_session) + "-" + str(start_session) + " " + str(
            user) + ". " + "Студия *****."
        self.comment_sevastopol_technical = str(start_tehnicheskogo_session) + "-" + str(start_session) + " " + str(
            user) + ". " + "Студия *****."
        # Атрибуты, которые будем push, с помощью метода, только рабочего сеанса
        self.video_type_id_rabochiy = '2'  # тип сеанса - рабочий
        self.seans_time_rabochiy = time_difference(start_session, finish_session)[0]
        self.trud_hours_rabochiy = time_difference(start_session, finish_session)[1]
        self.comment_simferopol_rabochiy = str(start_session) + "-" + str(
            finish_session) + " " + str(user) + ". " + "Студия *****."
        self.comment_sevastopol_rabochiy = str(start_session) + "-" + str(
            finish_session) + " " + str(user) + ". " + "Студия *****."

    def push(self):
        """
        Сейчас я буду пушить 4 записи,
        подставляя значения атрибутов экземпляра класса,
        в таком порядке:
        1. Технический *****
        2. Технический *****
        3. Рабочий *****
        4. Рабочий *****
        """
        push_zapis(self.seans_user_id, self.video_type_id_technical, self.video_com_type, self.video_place_id,
                   self.podr_id, self.seans_datetime_sel, self.seans_time_technical, self.trud_peoples,
                   self.trud_hours_technical, self.comment_simferopol_technical)
        push_zapis(self.seans_user_id, self.video_type_id_technical, self.video_com_type, self.video_place_id,
                   self.podr_id, self.seans_datetime_sel, self.seans_time_technical, self.trud_peoples,
                   self.trud_hours_technical, self.comment_sevastopol_technical)
        push_zapis(self.seans_user_id, self.video_type_id_rabochiy, self.video_com_type, self.video_place_id,
                   self.podr_id, self.seans_datetime_sel, self.seans_time_rabochiy, self.trud_peoples,
                   self.trud_hours_rabochiy, self.comment_simferopol_rabochiy)
        push_zapis(self.seans_user_id, self.video_type_id_rabochiy, self.video_com_type, self.video_place_id,
                   self.podr_id, self.seans_datetime_sel, self.seans_time_rabochiy, self.trud_peoples,
                   self.trud_hours_rabochiy, self.comment_sevastopol_rabochiy)


def create_spisok_zapisey(file="Zapis_uchet_k.txt"):
    """
    Функция чтение текстового файла и создание списка экземпляров класса zapis_uchet_k, возвращает список
    """
    with open(file) as f:
        zapis_number = []
        for line in f:
            line = line.strip()
            spisok_parametrov_convisation = line.split(" ")
            zapis_number.append(zapis_uchet_k(spisok_parametrov_convisation[0], spisok_parametrov_convisation[1],
                                              spisok_parametrov_convisation[2], spisok_parametrov_convisation[3],
                                              spisok_parametrov_convisation[4]))
    return zapis_number


def time_difference(value1, value2):
    """
    Получение разницы между временем в минутах, возвращает список сначала значение в минутах, затем в часах
    """
    date_format_value1 = datetime.strptime(value1, '%H:%M')
    date_format_value2 = datetime.strptime(value2, '%H:%M')
    seans_time = date_format_value2 - date_format_value1
    time_difference_in_minutes = seans_time / timedelta(minutes=1)
    time_difference_in_hours = seans_time / timedelta(hours=1)
    return int(time_difference_in_minutes), round(time_difference_in_hours, 1)


def push_zapis(seans_user_id, video_type_id, video_com_type_id, video_place_id, podr_id, seans_datetime_sel, seans_time,
               trud_peoples, trud_hours, comment):
    """
    Функция внесения записи в Учет-К
    """
    url_login = 'http://*****'
    session = requests.session()
    session.post(url_login, {  # Аутентификация в Учет-К
        'data[User][username]': '*****',
        'data[User][password]': '*****',
        'remember': 1,
    })

    str_comment = comment.encode('cp1251')
    a = session.post('http://*****', {  # Пример внесения записи(рабочий)
        'data[Video][seans_user_id]': seans_user_id,
        'data[Video][video_type_id]': video_type_id,
        'data[Video][video_com_type_id]': video_com_type_id,
        'data[Video][video_place_id]': video_place_id,
        'data[Video][podr_id]': podr_id,
        'data[Video][seans_datetime_sel]': seans_datetime_sel,
        'data[Video][seans_time]': seans_time,
        'data[Video][trud_peoples]': trud_peoples,
        'data[Video][trud_hours]': trud_hours,
        'data[Video][comment]': str_comment,
    })


def seans_user_id_init(abonent, file='Abonenti.txt'):
    """
    Функция создания словаря с ключами абонентами и значениями
    предназначения этих абонентов seans_user_id
    Возвращает seans_user_id абонента
    """
    seans_user_id_slovar = {}
    with open(file) as f:
        for line in f:
            line = line.strip()
            spisok_abonentov = line.split(" ")
            seans_user_id_slovar.update({spisok_abonentov[0]: spisok_abonentov[1]})
    seans_user_id_abonent = seans_user_id_slovar.get(abonent)
    return seans_user_id_abonent


"""
Непосредственно сама главная функция
"""
zapis_number = create_spisok_zapisey()  # Создаем список с экземпляроми класса из текстового файла "Zapis_uchet_k.txt"
i = 0
for item in zapis_number:  # Проходим по списку и активироем метод push каждого экземпляра класса, то есть пушим записи в соответсятвии с текстовым файлом
    zapis_number[i].push()
    i = i + 1