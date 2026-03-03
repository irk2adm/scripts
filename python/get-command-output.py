#!/usr/bin/env python3
"""
Получение вывода системной команды.

Этот скрипт показывает, как получить результат выполнения команды
в переменную для дальнейшей обработки.

Author: System Administrator
Date: 2026
"""

import subprocess


def get_command_output(command):
    """
    Выполняет команду и возвращает её вывод.
    
    Args:
        command (str): Команда для выполнения
    
    Returns:
        str: Вывод команды или сообщение об ошибке
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=10  # Максимум 10 секунд
        )
        
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Ошибка: {result.stderr}"
    
    except subprocess.TimeoutExpired:
        return "Ошибка: Команда выполнялась слишком долго"


# Основной блок выполнения
if __name__ == '__main__':
    # Получаем список процессов
    output = get_command_output('tasklist')  # Для Windows
    # output = get_command_output('ps aux')  # Для Linux/Mac
    
    print("Результат выполнения команды:")
    print(output[:500])  # Выводим первые 500 символов