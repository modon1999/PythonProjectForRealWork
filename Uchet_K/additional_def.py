from datetime import datetime
from datetime import timedelta

import requests


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
    Функция внесения записи в *****
    """
    url_login = 'http://*****'
    session = requests.session()
    session.post(url_login, {  # Аутентификация в *****
        'data[User][username]': '*****',
        'data[User][password]': '*****',
        'remember': 1,
    })

    str_comment = comment.encode('cp1251')
    session.post('http://*****', {  # Пример внесения записи(рабочий)
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
