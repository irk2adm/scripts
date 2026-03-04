#!/usr/bin/env python3


import os


def file_exists(path):
    """
    Функция принимает один аргумент path (строка)
    Возвращает True, если файл существует
    Возвращает False, если не существует
    """
    return os.path.exists(path)


# Тест
print(file_exists("./.tests/test.log"))
