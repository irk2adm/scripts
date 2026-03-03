#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Запуск системной команды.

Этот скрипт демонстрирует базовое использование subprocess
для выполнения команд операционной системы.

Author: System Administrator
Date: 2026
"""

import subprocess


def run_simple_command(command):
    """
    Выполняет системную команду и выводит результат.
    
    Args:
        command (str): Команда для выполнения
    
    Returns:
        None
    """
    # Запускаем команду
    subprocess.run(command, shell=True)


# Основной блок выполнения
if __name__ == '__main__':
    # Для Windows
    run_simple_command('dir')
    
    # Для Linux/Mac (раскомментировать при необходимости)
    # run_simple_command('ls -la')