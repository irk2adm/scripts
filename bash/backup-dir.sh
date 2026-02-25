#!/bin/bash

backup_dir() {
    # Проверка количества аргументов
    if [ $# -ne 2 ]; then
        echo "Использование: $0 <директория> <имя_архива>"
        return 1
    fi
    
    local dir=$1
    local archive_name=$2
    
    # Проверка существования директории
    if [ ! -d "$dir" ]; then
        echo "Ошибка: Директория '$dir' не существует"
        return 1
    fi

    # Создание архива с датой
    local archive_file="$archive_name-$(date +"%Y%m%d").tar.gz"
    if tar -czf "$archive_file" -C "$(dirname "$dir")" "$(basename "$dir")" 2>/dev/null; then
        echo "Архив создан: $archive_file"
        return 0
    else
        echo "Ошибка: не удалось создать архив"
        return 1
    fi
}

# Тестирование
backup_dir ".tests/" tests