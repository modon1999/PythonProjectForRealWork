import paramiko
import additional_def
import class_def_for_error_handling
import getpass

host = input("Введите ip-адресс удалённого сервера: ")
if False == class_def_for_error_handling.valid_ip(host):
    print("IP-адресс сервера некорректен!")
    exit()
user = input("Введите имя пользователя на удалённом сервере: ")
passwd = getpass.getpass("Введите пароль для аутентификаци на удалённом сервере: ")
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=host, username=user, password=passwd, port=port)
except paramiko.ssh_exception.AuthenticationException:
    print('Неправильно введено имя пользователя или пароль!')
    exit()
except paramiko.ssh_exception.NoValidConnectionsError:
    print('Сервер не найден, возможно вы ошиблись с написанием ip-адреса или он недостижим по 22 порту')
    exit()

additional_def.list_home_directory(client)
additional_def.quantity_files_in_home_directory(client)
additional_def.list_directory_in_home_directory(client)
additional_def.list_txt_files_in_home_directory(client)
additional_def.copied_file_in_home_directory(client, host, user, passwd)

client.close()
