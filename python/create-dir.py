#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создание директории, если она не существует.

Этот скрипт демонстрирует работу с модулем os для создания папок.
Проверяет существование директории перед созданием, чтобы избежать ошибок.

Author: System Administrator
Date: 2026
"""

import os


def create_directory(directory_name):
    """
    Создаёт директорию, если она не существует.
    
    Args:
        directory_name (str): Имя или путь к создаваемой директории
    
    Returns:
        tuple: (bool, str) - (успешно_создано, сообщение)
    """
    # Проверяем, существует ли директория
    if os.path.exists(directory_name):
        return False, f'Директория "{directory_name}" уже существует'
    
    # Создаём директорию
    try:
        os.mkdir(directory_name)
        return True, f'Директория "{directory_name}" успешно создана'
    except OSError as e:
        return False, f'Ошибка создания директории: {e}'


# Основной блок выполнения
if __name__ == '__main__':
    # Создаём папку для логов
    dir_name = 'logs'
    success, message = create_directory(dir_name)
    print(message)
    
    # Проверяем, что директория создана
    if success or os.path.exists(dir_name):
        print(f'Проверка: директория "{dir_name}" существует')