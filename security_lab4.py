from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import random


_IV456 = b'yo_esK1DOHg2x-3L'  # 16 байт
_SALT = b'8_TuDUK9IpJKaM7NWkpSQcMlVh0ZoEmYdeIOjvItOSk='
_LEN_BLOCK_SIZE = 16


def gen_user_secret_key(password: bytes) -> bytes:
    if isinstance(password, bytes) is False:
        raise TypeError(r"isinstance(password, bytes) is False")
    res = hashlib.pbkdf2_hmac(
        'sha256',
        password,
        _SALT,
        100000)
    return res


def hash_value(value: bytes) -> str:
    '''
    пользователь ввел пароль, генерируем ему хэш значение
    по паролю, возвращает хеш значение
    '''
    if isinstance(value, bytes) is False:
        raise TypeError(r"isinstance(value, bytes) is False")
    m = hashlib.sha256(_SALT + value)
    hashed_pas = m.hexdigest()
    return hashed_pas


def _fill_random_bytes(bytes_str: bytes, length: int) -> bytes:
    while len(bytes_str) % length != 0:  # должно быть кратно 16 байт
        symbol = bytes()
        if len(bytes_str) > 0:
            pos = random.randint(0, len(bytes_str))
            symbol = bytes_str[pos: pos + 1]
        bytes_str += symbol
    return bytes_str


def encrypt(message: bytes, key: bytes) -> bytes:
    if isinstance(message, bytes) is False:
        raise TypeError(r"isinstance(message, bytes) is False")
    if isinstance(key, bytes) is False:
        raise TypeError(r"isinstance(key, bytes) is False")

    len_block = len(message).to_bytes(length=_LEN_BLOCK_SIZE, byteorder='big')
    message = len_block + message
    # должно быть кратно 16 байт
    message = _fill_random_bytes(message, _LEN_BLOCK_SIZE)
    obj = AES.new(key, AES.MODE_CBC, _IV456)
    ciphertext = obj.encrypt(message)

    return ciphertext


def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    if isinstance(ciphertext, bytes) is False:
        raise TypeError(r"isinstance(ciphertext, bytes) is False")
    if isinstance(key, bytes) is False:
        raise TypeError(r"isinstance(key, bytes) is False")
    if len(ciphertext) % _LEN_BLOCK_SIZE != 0:
        raise ValueError(r"len(bytes_str) % length != 0")

    # ciphertext = _fill_random_bytes(ciphertext, _LEN_BLOCK_SIZE)

    obj = AES.new(key, AES.MODE_CBC, _IV456)
    text = obj.decrypt(ciphertext)

    size = int.from_bytes(text[:_LEN_BLOCK_SIZE], byteorder='big')
    text = text[_LEN_BLOCK_SIZE:size + _LEN_BLOCK_SIZE]

    return text


def gen_secret_key() -> bytes:
    '''
    генерирует ключ для шифрования заметок, ключ генерируется для алгоритма AES
    '''
    # длина ключа AES равна 16, 24, или 32 байтам.
    return Random.new().read(32)


if __name__ == "__main__":
    pass
    # print(SHA256.new("1".encode(encoding='utf-8')).hexdigest())
    # или
    # print(hashlib.sha256("1".encode(encoding='utf-8')).hexdigest())

    '''
    message = "hi"

    sk = gen_secret_key() #сгенерировали рандомное байты
    message = bytes(message, 'utf-8') # перевели сообщение в байты

    passw = bytes('123', 'utf-8') # сгенерировали ключ на основе
    пользовательского пароля

    sk1 = gen_user_secret_key(passw) # сгенерировали ключ на основе
    пользовательского пароля
    dc = encrypt(sk,sk1) # зашифровали рандомные байты  помощью
    пользовательского пароля

    dc = dc.hex()
    dc = bytes.fromhex(dc)

    dc = decrypt(dc, sk1) # расшифровали рандомные байты с помощью ключа на
    основе пользовательского праоля

    mdc = encrypt(message,sk) # зашифровали соообщение рандомными байтами
    message = decrypt(mdc, dc) # расшифровали сообщение рандомными байтами
    message = message.decode('utf-8') # перевели байтовое сообщение в строку
    print(message) # вернули изначальное сообщение

    '''
    '''
    мы сгенерировали хеш значение,
    программа автоматически сгенерировала имя папки по имени пользователя #
    дальше она сгенерировала ключик с помощью функции ген секрет кей #
    теперь его надо зашифровать с помощью мастер ключа ген юзер секрет кей
    возвращает мастер ключ
    теперь необходимо зашифровать мастер ключ с помощью шифрования енкрипт и
    декрипт  #
    '''

    '''
    ключ генерируется в 2 этапа сначала с помощью ген секрет кей этот
    ключ будет зашифрован с помощью ключа сгенерированного на основе
    пароля пользователя
    для того чтобы зашифровать по ключу пользователя необходимо
    сгенерировать специальный мастер ключ   ген юзер секрет кейспец
    алшгоритм для генерации ключей на соновании паролей
    в результате получили ключ на основании пользовательского пароля
    и с помощью этого ключа мы уже шифруем ключ шифрования
    в енкрипт сообщение это секрет кей а ключ это ген секрет юзер кей
    с расшифровкой то же самое передаем зашифрованный текст передаем
    ключ
    '''
    '''
    password = '123'
    password_bytes = encode(password,'utf-8')
    hashed_password = hash_value(password_bytes)
    sk = gen_secret_key()
    sk1 = gen_user_secret_key(password_bytes)
    master_key = encrypt(sk, sk1)
    master_key_hex = master_key.hex()
    master_key_bytes = bytes.fromhex(master_key_hex)
    master_key_decrypt = decrypt(master_key_bytes, sk1) 
    '''