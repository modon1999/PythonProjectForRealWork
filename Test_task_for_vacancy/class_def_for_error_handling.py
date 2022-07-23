def valid_ip(address):
    """
    Функция проверки правильности формата написания ip-адреса
    """
    try:
        host_bytes = address.split('.')
        valid = [int(b) for b in host_bytes]
        valid_correct = []
        for item in valid:
            if item >= 0 and item <= 255:
                valid_correct.append(item)
        return len(host_bytes) == 4 and len(valid_correct) == 4
    except:
        return False
