#!/bin/bash

create_backup() {
  # Принимает 2 аргумента — путь к директории и имя архива
  # Проверяет, что оба аргумента переданы
  # Проверяет, существует ли директория
  # Создаёт архив в формате .tar.gz с именем [имя_архива].tar.gz
  # Возвращает 0 при успехе, 1 при ошибке

  # Проверка аргументов
  if [ ! $# -eq 2 ]; then
    echo "Ошибка: Должно быть 2 аргумента (путь к директории и имя архива)"
    return 1
  fi

  # Проверка директории
  if [ ! -d "$1" ]; then
    echo "Ошибка: такой директории нет"
    return 1
  fi
  
  # Создание архива c проверкой
  if ! tar -czf "$2.tar.gz" -C "$(dirname "$1")" "$(basename "$1")"; then
    echo "Ошибка: не удалось создать архив"
    return 1
  fi
  return 0
}

# Тест
create_backup .tests/ backup_log    # Создаст backup_log.tar.gz
create_backup /nonexistent test  # Ошибка
create_backup                    # Ошибка