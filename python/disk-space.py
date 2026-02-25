import os
import shutil


def check_disk_space(path='/'):
    """
    Проверяет свободное место на диске.

    Args:
        path (str): Путь к файловой системе

    Returns:
        dict: Словарь с информацией о диске
    """
    # Получаем статистику диска
    stat = shutil.disk_usage(path)

    total_gb = stat.total / (1024**3)
    used_gb = stat.used / (1024**3)
    free_gb = stat.free / (1024**3)
    percent_used = (used_gb / total_gb) * 100

    return {
        'total': round(total_gb, 2),
        'used': round(used_gb, 2),
        'free': round(free_gb, 2),
        'percent_used': round(percent_used, 2)
    }


# Использование
# result = check_disk_space('C:\\')  # Для Windows
result = check_disk_space('/')   # Для Linux/Mac

print(f"Всего: {result['total']} GB")
print(f"Использовано: {result['used']} GB ({result['percent_used']}%)")
print(f"Свободно: {result['free']} GB")
