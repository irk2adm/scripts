import os


# 1. Определение функции
def count_log_files(folder_path):
    """
    Считает количество файлов с расширением .log в указанной папке.

    Args:
        folder_path (str): Путь к папке

    Returns:
        int: Количество .log файлов
    """

    # 2. Тело функции
    files = os.listdir(folder_path)
    count = 0

    for file in files:
        if file.endswith('.log'):
            count += 1

    return count


# 3. Тестовый код (выполняется при запуске файла)
if __name__ == '__main__':
    result = count_log_files('.')
    print(f'Найдено .log файлов: {result}')
