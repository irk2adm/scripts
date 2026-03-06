#!/usr/bin/env python3

import subprocess


def get_command_output(command):
    """
    Принимает строку с командой
    Возвращает строку с выводом команды (то, что команда напечатала в консоль)
    Если команда завершилась с ошибкой, верните пустую строку ''
    """
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return ''


# Тесты
get_command_output("echo 123")
