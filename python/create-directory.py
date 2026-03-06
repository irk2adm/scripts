#!/usr/bin/env python3

import os


def create_directory(path):
    """
    функция создаёт директорию

    Принимает путь к директории
    Если директория уже существует - возвращает False
    Если директория создана успешно - возвращает True
    Если ошибка (нет прав, недопустимое имя) - возвращает False
    """
    if os.path.exists(path):
        return False

    try:
        os.mkdir(path)
        return True
    except OSError:
        return False


# Тесты
create_directory("test1")
