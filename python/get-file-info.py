#!/usr/bin/env python3

import os


def get_file_info(path):
    """
    Возвращает информацию о файле
    Возвращает словарь с ключами:
        'exists': True/False (существует ли файл)
        'is_file': True/False (это файл, а не папка)
        'size': размер файла в байтах (если существует, иначе None)
    """
    exists = os.path.exists(path)

    if exists:
        is_file = os.path.isfile(path)
        size = os.path.getsize(path)
        return {
            'exists': exists,
            'is_file': is_file,
            'size': size
        }
    else:
        return {
            'exists': exists,
            'is_file': None,
            'size': None
        }


# Тест
print(get_file_info('.tests/test1.log'))
