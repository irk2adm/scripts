#!/usr/bin/env python3

import subprocess


def run_command(command):
    """
    Принимает строку с командой (например, 'dir' или 'ls')
    Возвращает True, если команда выполнена успешно (код возврата 0)
    Возвращает False, если команда завершилась с ошибкой
    """
    result = subprocess.run(command, shell=True)
    return result.returncode == 0


# Тесты
run_command("ls")
run_command("dir")
