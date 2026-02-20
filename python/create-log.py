# Создаём тестовый лог-файл
with open('test.log', 'w') as f:
    f.write('INFO: Старт приложения\n')
    f.write('ERROR: Не удалось подключиться к БД\n')
    f.write('INFO: Повторная попытка\n')
    f.write('ERROR: Таймаут соединения\n')
    f.write('INFO: Завершение работы\n')

print('Тестовый файл создан!')