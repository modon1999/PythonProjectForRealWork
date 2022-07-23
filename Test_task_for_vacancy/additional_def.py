def list_home_directory(client):
    """
    Функция вывода содержимого домашней директории удалённого сервера, а вход получает клиента с
    установленным соединением. Вывод осуществляется в консоль.
    """
    stdin, stdout, stderr = client.exec_command("ls ~")
    list_content_home_directory = stdout.read()
    list_content_home_directory = list_content_home_directory.decode()
    print('Список содержимого домашней директории: \n' + list_content_home_directory)


def quantity_files_in_home_directory(client):
    """
    Функция подсчета файлов и директорий в домашней директории удалённого сервера, на вход получает клиента с
    установленным соединением. Вывод осуществляется в консоль.
    """
    stdin, stdout, stderr = client.exec_command("ls -d ~/* | wc -l")
    quantity_files_in_home_directory = stdout.read()
    quantity_files_in_home_directory = quantity_files_in_home_directory.decode()
    print('Общее количество файлов домашней директории: ' + quantity_files_in_home_directory)


def list_directory_in_home_directory(client):
    """
    Функция подсчета файлов и директорий в директориях домашней директории(вложенность 2) удалённого сервера,
    на вход получает клиента с установленным соединением. Вывод осуществляется в консоль.
    """
    stdin, stdout, stderr = client.exec_command("ls -l ~ | grep ^d | awk '{print $9}'")
    list_directory_in_home_directory = stdout.read()
    list_directory_in_home_directory = list_directory_in_home_directory.decode()
    list_directory_in_home_directory = list_directory_in_home_directory.split('\n')
    list_directory_in_home_directory = [x for x in list_directory_in_home_directory if x]  # удаляем пустой элемент
    for directory in list_directory_in_home_directory:
        stdin, stdout, stderr = client.exec_command(f"ls -d ~/{directory}/* | wc -l")
        quantity_files_in_directory = stdout.read()
        quantity_files_in_directory = quantity_files_in_directory.decode()
        print('В ' + directory + ' домашней поддериктории данное количество файлов: ' + quantity_files_in_directory)
    if list_directory_in_home_directory == []:
        print("В домашней директории отсутствуют поддиректории!")


def list_txt_files_in_home_directory(client):
    """
    Функция создает копии файлов формата *.txt в формате tmp_*.txt в домашней директории удалённого сервера,
    на вход получает клиента с установленным соединением. Вывод не осуществляется.
    """
    stdin, stdout, stderr = client.exec_command(
        "ls -l ~ | grep .txt | grep -v tmp_ | awk '{print $9}'")  # чтобы не плодить tmp-файлы до бесконечности
    list_txt_files_in_home_directory = stdout.read()
    list_txt_files_in_home_directory = list_txt_files_in_home_directory.decode()
    list_txt_files_in_home_directory = list_txt_files_in_home_directory.split('\n')
    list_txt_files_in_home_directory = [x for x in list_txt_files_in_home_directory if x]  # удаляем пустой элемент

    for txt_file in list_txt_files_in_home_directory:
        stdin, stdout, stderr = client.exec_command(
            f"cp ~/{txt_file} ~/tmp_{txt_file}")
    if list_txt_files_in_home_directory == []:
        print("В домашней директории отсутствуют файлы формата *.txt!")
    else:
        print("Для файлов формата *.txt созданы копии формата tmp_*.txt.")


def copied_file_in_home_directory(client, host, user, passwd):
    """
    Функция копирует файл copied_file в домашней директории удаленного сервера в рабочую директорию скрипта и заменяет
    в полученном файле плейсхолдер ip_server - ip хоста, username - имя пользователя,
    password - пароль для аутентификации. На вход принимает клиента с установленным соединением,
    а также параметры для замены которые он берёт при аутентификации на сервере.
    Примерный вид файла на удалённом сервере:
    Пароль для сервера {ip_server} для пользователя {username}: {password}
    Осуществляется вывод в консоль о том, что был скопипован файл
    """
    stdin, stdout, stderr = client.exec_command("cat ~/copied_file")
    copied_file_in_home_directory = stdout.read()
    error_message = stderr.read()
    error_message = error_message.decode()
    if error_message != '':
        print(
            "Файл copied_file не существует в домашней директории удалённого сервера, скопировать его с заменой плейсхолдеров неудалось!")
        exit()
    copied_file_in_home_directory = copied_file_in_home_directory.decode()
    list_placeholders = ['{ip_server}', '{username}', '{password}']
    for placeholder in list_placeholders:
        if placeholder not in copied_file_in_home_directory:
            print("В файле copied_file отсутствуют все необходимые плейсхолдеры! Он будет будет копирован с ошибками!")
            break
    copied_file_in_home_directory = copied_file_in_home_directory.format(ip_server=host, username=user, password=passwd)
    create_file = open("copied_file", "w+")
    create_file.write(copied_file_in_home_directory)
    create_file.close()
    print(
        "Скопирован файл copied_file из домашней директории удаленного сервера в рабочую директорию скрипта с заменой плейсхолдеров")
