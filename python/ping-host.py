#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Проверка доступности хоста через ping.

Этот скрипт использует subprocess для выполнения команды ping
и проверяет, доступен ли удалённый хост.

Author: System Administrator
Date: 2026
"""

import subprocess


def ping_host(host, count=2):
    """
    Проверяет доступность хоста через ping.
    
    Args:
        host (str): IP-адрес или доменное имя
        count (int): Количество пакетов для отправки
    
    Returns:
        bool: True если хост доступен, False если недоступен
    """
    # Формируем команду в зависимости от ОС
    # Windows использует -n, Linux/Mac используют -c
    command = f'ping -n {count} {host}'  # Для Windows
    
    # Запускаем команду, скрываем вывод
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    
    # Возвращаем код завершения (0 = успешно)
    return result.returncode == 0


# Основной блок выполнения
if __name__ == '__main__':
    host = '8.8.8.8'
    
    if ping_host(host):
        print(f'Хост {host} доступен')
    else:
        print(f'Хост {host} недоступен')