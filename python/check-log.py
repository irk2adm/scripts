def check_log(file_path):
    """Функция читает файл и считает строки с 'ERROR'"""
    error_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                error_count += 1

    return error_count


# Использование функции
logs = ['test.log']

for log_file in logs:
    errors = check_log(log_file)
    print(f"В файле {log_file}: {errors} ошибок")
