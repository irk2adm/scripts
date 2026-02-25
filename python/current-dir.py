#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Получение текущей рабочей директории.

Этот скрипт показывает, как получить путь к текущей директории,
в которой выполняется Python-скрипт.

Author: System Administrator
Date: 2026
"""

import os


def get_current_directory():
    """
    Возвращает путь к текущей рабочей директории.
    
    Returns:
        str: Абсолютный путь к текущей директории
    """
    return os.getcwd()


# Основной блок выполнения
if __name__ == '__main__':
    current_dir = get_current_directory()
    print(f'Текущая рабочая директория: {current_dir}')