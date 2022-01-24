import additional_def
import class_def_for_error_handling


class Zapis_uchet_k:
    """
    Инициализация класса для создания экземпляров записи и метода push в *****
    """

    def __init__(self, user, date, start_tehnicheskogo_session, start_session, finish_session, video_com_type,
                 video_place_id,
                 dislocation):  # dislocation: по умолчанию 1 - Си*****+Се*****, 2 - Си*****, 3 - Се*****
        # Атрибуты с которыми будем работать
        self.comment_SC_PPP_RF = 'Студия СЦ ***** в городе Си*****'
        self.comment_GFI = 'Студия ГФИ в городе Се*****'
        self.dislocation = dislocation
        self.user = user
        self.date = date
        self.start_tehnicheskogo_session = start_tehnicheskogo_session
        self.start_session = start_session
        self.finish_session = finish_session
        # Атрибуты, которые будем push, с помощью метода, общие
        self.seans_user_id = seans_user_id_init(user)
        self.video_com_type = video_com_type  # по умолчанию 1 - ЗВС, 2 - КВС, 3 - ЗВС+КВС
        self.video_place_id = video_place_id  # по умолчанию 1 - студия *****, 2 - СЦ *****, 10 - ГФИ *****
        self.podr_id = '1207692237'  # всегда *****
        self.seans_datetime_sel = date  # дата проведения
        self.trud_peoples = '1'  # количество людей всегда 1
        # Атрибуты, которые будем push, с помощью метода, только технического сеанса
        self.video_type_id_technical = '1'  # тип сеанса - технический
        self.seans_time_technical = additional_def.time_difference(start_tehnicheskogo_session, start_session)[0]
        self.trud_hours_technical = additional_def.time_difference(start_tehnicheskogo_session, start_session)[1]
        if int(self.video_place_id) == 2:
            self.comment_simferopol_technical = str(start_tehnicheskogo_session) + "-" + str(start_session) + " " + str(
                user) + ". " + self.comment_SC_PPP_RF
        else:
            self.comment_simferopol_technical = str(start_tehnicheskogo_session) + "-" + str(start_session) + " " + str(
                user) + ". " + "Студия *****."
        if int(self.video_place_id) == 10:
            self.comment_sevastopol_technical = str(start_tehnicheskogo_session) + "-" + str(start_session) + " " + str(
                user) + ". " + self.comment_GFI
        else:
            self.comment_sevastopol_technical = str(start_tehnicheskogo_session) + "-" + str(start_session) + " " + str(
                user) + ". " + "Студия *****."
        # Атрибуты, которые будем push, с помощью метода, только рабочего сеанса
        self.video_type_id_rabochiy = '2'  # тип сеанса - рабочий
        self.seans_time_rabochiy = additional_def.time_difference(start_session, finish_session)[0]
        self.trud_hours_rabochiy = additional_def.time_difference(start_session, finish_session)[1]
        if int(self.video_place_id) == 2:
            self.comment_simferopol_rabochiy = str(start_session) + "-" + str(
                finish_session) + " " + str(user) + ". " + self.comment_SC_PPP_RF
        else:
            self.comment_simferopol_rabochiy = str(start_session) + "-" + str(
                finish_session) + " " + str(user) + ". " + "Студия *****."
        if int(self.video_place_id) == 10:
            self.comment_sevastopol_rabochiy = str(start_session) + "-" + str(
                finish_session) + " " + str(user) + ". " + self.comment_GFI
        else:
            self.comment_sevastopol_rabochiy = str(start_session) + "-" + str(
                finish_session) + " " + str(user) + ". " + "Студия *****."

    def push(self):
        """
        Пушим записи, подставляя значения атрибутов экземпляра класса
        """
        if int(self.dislocation) == 1:
            additional_def.push_zapis(self.seans_user_id, self.video_type_id_technical, self.video_com_type,
                                      self.video_place_id,
                                      self.podr_id, self.seans_datetime_sel, self.seans_time_technical,
                                      self.trud_peoples,
                                      self.trud_hours_technical, self.comment_simferopol_technical)
            additional_def.push_zapis(self.seans_user_id, self.video_type_id_technical, self.video_com_type,
                                      self.video_place_id,
                                      self.podr_id, self.seans_datetime_sel, self.seans_time_technical,
                                      self.trud_peoples,
                                      self.trud_hours_technical, self.comment_sevastopol_technical)
            additional_def.push_zapis(self.seans_user_id, self.video_type_id_rabochiy, self.video_com_type,
                                      self.video_place_id,
                                      self.podr_id, self.seans_datetime_sel, self.seans_time_rabochiy,
                                      self.trud_peoples,
                                      self.trud_hours_rabochiy, self.comment_simferopol_rabochiy)
            additional_def.push_zapis(self.seans_user_id, self.video_type_id_rabochiy, self.video_com_type,
                                      self.video_place_id,
                                      self.podr_id, self.seans_datetime_sel, self.seans_time_rabochiy,
                                      self.trud_peoples,
                                      self.trud_hours_rabochiy, self.comment_sevastopol_rabochiy)
        elif int(self.dislocation) == 2:
            additional_def.push_zapis(self.seans_user_id, self.video_type_id_technical, self.video_com_type,
                                      self.video_place_id, self.podr_id, self.seans_datetime_sel,
                                      self.seans_time_technical,
                                      self.trud_peoples, self.trud_hours_technical, self.comment_simferopol_technical)
            additional_def.push_zapis(self.seans_user_id, self.video_type_id_rabochiy, self.video_com_type,
                                      self.video_place_id,
                                      self.podr_id, self.seans_datetime_sel, self.seans_time_rabochiy,
                                      self.trud_peoples,
                                      self.trud_hours_rabochiy, self.comment_simferopol_rabochiy)
        elif int(self.dislocation) == 3:
            additional_def.push_zapis(self.seans_user_id, self.video_type_id_technical, self.video_com_type,
                                      self.video_place_id,
                                      self.podr_id, self.seans_datetime_sel, self.seans_time_technical,
                                      self.trud_peoples,
                                      self.trud_hours_technical, self.comment_sevastopol_technical)
            additional_def.push_zapis(self.seans_user_id, self.video_type_id_rabochiy, self.video_com_type,
                                      self.video_place_id,
                                      self.podr_id, self.seans_datetime_sel, self.seans_time_rabochiy,
                                      self.trud_peoples,
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
            try:
                class_def_for_error_handling.check_video_com_type(
                    spisok_parametrov_convisation[5])  # Функция проверки параметра типа сеанса
            except IndexError:
                spisok_parametrov_convisation.insert(5, '1')  # По умолчанию выводит ЗВС
            try:
                class_def_for_error_handling.check_video_place_id(
                    spisok_parametrov_convisation[6])  # Функция проверки параметра места проведения сеанса
            except IndexError:
                spisok_parametrov_convisation.insert(6, '1')  # По умолчанию выводит студию *****
            try:
                class_def_for_error_handling.check_dislocation(
                    spisok_parametrov_convisation[7])  # Функция проверки параметра дислокации сеанса
            except IndexError:
                spisok_parametrov_convisation.insert(7, '1')  # По умолчанию выводит Си***** + Се*****
            if len(spisok_parametrov_convisation) not in range(5,
                                                               9):  # Обработка ошибок в текстовом файле Zapis_uchet_k.txt
                try:
                    raise class_def_for_error_handling.False_in_file_zapis_uchet_k()
                except class_def_for_error_handling.False_in_file_zapis_uchet_k:
                    class_def_for_error_handling.notification("Ошибка в текстовом файле Zapis_uchet_k.txt",
                                                              "Проверьте количество параметров в строке " + str(
                                                                  iteration_number) + "!")
                    exit()
            try:
                if int(spisok_parametrov_convisation[6]) == 2:
                    spisok_parametrov_convisation[5] = '2'
                    spisok_parametrov_convisation[7] = '2'
                elif int(spisok_parametrov_convisation[6]) == 10:
                    spisok_parametrov_convisation[5] = '2'
                    spisok_parametrov_convisation[7] = '3'
            except IndexError:
                pass
            zapis_number.append(Zapis_uchet_k(spisok_parametrov_convisation[0], spisok_parametrov_convisation[1],
                                              spisok_parametrov_convisation[2], spisok_parametrov_convisation[3],
                                              spisok_parametrov_convisation[4], spisok_parametrov_convisation[5],
                                              spisok_parametrov_convisation[6], spisok_parametrov_convisation[7], ))
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
                    raise class_def_for_error_handling.False_in_file_abonenti()
                except class_def_for_error_handling.False_in_file_abonenti:
                    class_def_for_error_handling.notification("Ошибка в текстовом файле Abonenti.txt",
                                                              "Проверьте количество параметров в строке " + str(
                                                                  iteration_number) + "!")
                    exit()
            try:  # Обработка ошибок значения второго параметра в строке с строке в текстовом файле Abonenti.txt
                if int(spisok_abonentov[1]) not in range(1, 15):
                    raise class_def_for_error_handling.Diapozon_value_error()
            except class_def_for_error_handling.Diapozon_value_error:
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
