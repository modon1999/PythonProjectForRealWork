"""
------------------------------------------------------------------------------------------------------------
Задача: автоматизовать процесс заполнения учетных записей сеансов в Web-интерфейсе
Исполнение: ввиду разделения сетей из соображения безопасности возможности брать данные непостредственно
с защищенной сети не представляется возможным, поэтому оператору придется вручную заполнять
файл Zapis_uchet_k.txt с записями по образцу:
ФАМИЛИЯ_АБОНЕНТА ДАТА_СЕАНСА нАЧАЛО_ТЕХНИЧЕСКОГО_СЕАНСА НАЧАЛО_СЕАНСА кОНЕЦ_СЕАНСа
Также в файле Abonenti.txt содержится соответствие АБОНЕНТ:ПРИНАДЛЕЖНОСТЬ для работы программы, перед
запуском обязательно проверьте, есть ли этот абонент в текстовом файле, при необходимости внесите
изменения в файл по принципу соответствия, при желании в программе можно изменить конечный текстовый файл.
------------------------------------------------------------------------------------------------------------
Version 1.0 17.01.2022 Исполнил: Григорьев Н.С
Первая версия программы, все реализовано в виде функций и классов для масштабируемости кода, подробнее можно
рассмотреть в самом коде, комментарии написаны явно.Из недостатков отмечаю отсутствие обработки ошибок,можно
доработать
------------------------------------------------------------------------------------------------------------
Version 1.1 21.01.2022 Исполнил: Григорьев Н.С
Проведена обработка возможных ошибок в написании текстовых файлов, также для удобства масшабирования
программа была разнесена по нескольким файлам:
main.py - файл с главной функцией
additional_def.py - вспомогательные функции
class_def_for_error_handling.py - классы и функции для обработки ошибок
class_for_create_zapis.py - класс формирования записей и функции чтения файлов
------------------------------------------------------------------------------------------------------------
Version 2.0 24.01.2022 Исполнил: Григорьев Н.С
Добавлен новый функционал в виде 3-х необязательных параметров класса для записей:
video_com_type - тип сеанса: по умолчанию 1 - ЗВС, 2 - КВС, 3 - ЗВС+КВС
video_place_id - по умолчанию 1 - студия *****, 2 - СЦ *****, 10 - ГФИ *****
dislocation - по умолчанию 1 - Си*****+Се*****ь, 2 - Си*****ь, 3 - Се*****
Используются для отдельных сеансов. При это в программе существует ограничение: СЦ ***** -
только КВС в Си*****, ГФИ ***** - только КВС в городе Се*****
Таким образом файл Zapis_uchet_k.txt заполняется:
ФАМИЛИЯ_АБОНЕНТА ДАТА_СЕАНСА нАЧАЛО_ТЕХНИЧЕСКОГО_СЕАНСА НАЧАЛО_СЕАНСА кОНЕЦ_СЕАНСа ТИП_СЕАНСА* СТУДИЯ_СЕАНСА* ГОРОД_ПРОВЕДЕНИЯ*
Файл Abonenti.txt заполняется:
АБОНЕНТ_1 1
ФБОНЕНТ_2 7
------------------------------------------------------------------------------------------------------------
"""
import class_for_create_zapis

"""
Непосредственно сама главная функция
"""
zapis_number = class_for_create_zapis.create_spisok_zapisey()  # Создаем список с экземпляроми класса из текстового файла "Zapis_uchet_k.txt"
i = 0
for item in zapis_number:  # Проходим по списку и активироем метод push каждого экземпляра класса, то есть пушим записи в соответсятвии с текстовым файлом
    zapis_number[i].push()
    i = i + 1
