#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Проверка существования файлов и папок.

Этот скрипт демонстрирует работу с модулем os:
- Проверка существования файлов
- Определение типа (файл или папка)
- Проверка системных директорий

Author: System Administrator
Date: 2026
"""

import os


def check_file(path):
    """
    Проверяет существование и тип файла/папки.
    
    Args:
        path (str): Путь к файлу или папке
    
    Returns:
        str: Описание результата
    """
    if not os.path.exists(path):
        return f'{path} не найден!'
    
    if os.path.isfile(path):
        return f'{path} - это файл'
    
    if os.path.isdir(path):
        return f'{path} - это папка'
    
    return f'{path} - неизвестный тип'


# Основной блок выполнения
if __name__ == '__main__':
    # Проверяем тестовый файл
    print(check_file('test.log'))
    
    # Проверяем системную папку
    print(check_file('C:\\Windows'))