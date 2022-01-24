import additional_def
import class_def_for_error_handling


class zapis_uchet_k:
    """
    Инициализация класса для создания экземпляров записи и метода push в *****
    """

    def __init__(self, user, date, start_tehnicheskogo_session, start_session, finish_session):
        # Атрибуты с которыми будем работать
        self.user = user
        self.date = date
        self.start_tehnicheskogo_session = start_tehnicheskogo_session
        self.start_session = start_session
        self.finish_session = finish_session
        # Атрибуты, которые будем push, с помощью метода, общие
        self.seans_user_id = seans_user_id_init(user)
        self.video_com_type = '1'  # пока только ЗВС
        self.video_place_id = '1'  # пока по умолчанию *****
        self.podr_id = '1207692237'  # всегда *****
        self.seans_datetime_sel = date  # дата проведения
        self.trud_peoples = '1'  # количество людей всегда 1
        # Атрибуты, которые будем push, с помощью метода, только технического сеанса
        self.video_type_id_technical = '1'  # тип сеанса - технический
        self.seans_time_technical = additional_def.time_difference(start_tehnicheskogo_session, start_session)[0]
        self.trud_hours_technical = additional_def.time_difference(start_tehnicheskogo_session, start_session)[1]
        self.comment_simferopol_technical = str(start_tehnicheskogo_session) + "-" + str(start_session) + " " + str(
            user) + ". " + "Студия *****."
        self.comment_sevastopol_technical = str(start_tehnicheskogo_session) + "-" + str(start_session) + " " + str(
            user) + ". " + "Студия *****."
        # Атрибуты, которые будем push, с помощью метода, только рабочего сеанса
        self.video_type_id_rabochiy = '2'  # тип сеанса - рабочий
        self.seans_time_rabochiy = additional_def.time_difference(start_session, finish_session)[0]
        self.trud_hours_rabochiy = additional_def.time_difference(start_session, finish_session)[1]
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
        additional_def.push_zapis(self.seans_user_id, self.video_type_id_technical, self.video_com_type,
                                  self.video_place_id,
                                  self.podr_id, self.seans_datetime_sel, self.seans_time_technical, self.trud_peoples,
                                  self.trud_hours_technical, self.comment_simferopol_technical)
        additional_def.push_zapis(self.seans_user_id, self.video_type_id_technical, self.video_com_type,
                                  self.video_place_id,
                                  self.podr_id, self.seans_datetime_sel, self.seans_time_technical, self.trud_peoples,
                                  self.trud_hours_technical, self.comment_sevastopol_technical)
        additional_def.push_zapis(self.seans_user_id, self.video_type_id_rabochiy, self.video_com_type,
                                  self.video_place_id,
                                  self.podr_id, self.seans_datetime_sel, self.seans_time_rabochiy, self.trud_peoples,
                                  self.trud_hours_rabochiy, self.comment_simferopol_rabochiy)
        additional_def.push_zapis(self.seans_user_id, self.video_type_id_rabochiy, self.video_com_type,
                                  self.video_place_id,
                                  self.podr_id, self.seans_datetime_sel, self.seans_time_rabochiy, self.trud_peoples,
                                  self.trud_hours_rabochiy, self.comment_sevastopol_rabochiy)


def create_spisok_zapisey(file="Zapis_uchet_k.txt"):
    """
    Функция чтение текстового файла и создание списка экземпляров класса zapis_uchet_k, возвращает список
    """
    with open(file) as f:
        zapis_number = []
        for iteration_number, line in enumerate(f, 1):
            line = line.strip()
            if len(line) == 0:  # Если строка пуста, то пропускает её
                continue
            spisok_parametrov_convisation = line.split(" ")
            class_def_for_error_handling.check_date(spisok_parametrov_convisation[1],
                                                    iteration_number)  # Функция проверки параметра даты
            class_def_for_error_handling.check_time(spisok_parametrov_convisation[2],
                                                    iteration_number)  # Функция проверки параметра времени начала технического сеанса
            class_def_for_error_handling.check_time(spisok_parametrov_convisation[3],
                                                    iteration_number)  # Функция проверки параметра времени начала рабочего сеанса
            class_def_for_error_handling.check_time(spisok_parametrov_convisation[4],
                                                    iteration_number)  # Функция проверки параметра времени окончания сеанса
            if len(spisok_parametrov_convisation) != 5:  # Обработка ошибок в текстовом файле Zapis_uchet_k.txt
                try:
                    raise class_def_for_error_handling.false_in_file_zapis_uchet_k()
                except class_def_for_error_handling.false_in_file_zapis_uchet_k:
                    class_def_for_error_handling.notification("Ошибка в текстовом файле Zapis_uchet_k.txt",
                                                              "Проверьте количество параметров в строке " + str(
                                                                  iteration_number) + "!")
                    exit()
            zapis_number.append(zapis_uchet_k(spisok_parametrov_convisation[0], spisok_parametrov_convisation[1],
                                              spisok_parametrov_convisation[2], spisok_parametrov_convisation[3],
                                              spisok_parametrov_convisation[4]))
    return zapis_number


def seans_user_id_init(abonent, file='Abonenti.txt'):
    """
    Функция создания словаря с ключами абонентами и значениями
    предназначения этих абонентов seans_user_id
    Возвращает seans_user_id абонента
    """
    seans_user_id_slovar = {}
    with open(file) as f:
        for iteration_number, line in enumerate(f, 1):
            line = line.strip()
            if len(line) == 0:  # Если строка пуста, то пропускает её
                continue
            spisok_abonentov = line.split(" ")
            if len(spisok_abonentov) != 2:  # Обработка ошибок количество параметров с строке в текстовом файле Abonenti.txt
                try:
                    raise class_def_for_error_handling.false_in_file_abonenti()
                except class_def_for_error_handling.false_in_file_abonenti:
                    class_def_for_error_handling.notification("Ошибка в текстовом файле Abonenti.txt",
                                                              "Проверьте количество параметров в строке " + str(
                                                                  iteration_number) + "!")
                    exit()
            try:  # Обработка ошибок значения второго параметра в строке с строке в текстовом файле Abonenti.txt
                if int(spisok_abonentov[1]) not in range(1, 15):
                    raise class_def_for_error_handling.diapozon_value_error()
            except class_def_for_error_handling.diapozon_value_error:
                class_def_for_error_handling.notification("Ошибка в текстовом файле Abonenti.txt",
                                                          "Проверьте значение параметра типа пользователся в строке " + str(
                                                              iteration_number) + "! Оно должно быть в диапозоне от 1 до 14!")
                exit()
            except ValueError:
                class_def_for_error_handling.notification("Ошибка в текстовом файле Abonenti.txt",
                                                          "Проверьте значение параметра типа пользователся в строке " + str(
                                                              iteration_number) + "! Это должно быть число в диапозоне от 1 до 14!")
                exit()
            seans_user_id_slovar.update({spisok_abonentov[0]: spisok_abonentov[1]})
    seans_user_id_abonent = seans_user_id_slovar.get(abonent)
    class_def_for_error_handling.check_user(seans_user_id_abonent)  # Проверка соответствия пользователя
    return seans_user_id_abonent
