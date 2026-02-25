#!/bin/bash

parse_logs() {
  local log_file=$1
  local keyword=$2

  # Проверяем аргументы
  if [ -z "$log_file" ] || [ -z "$keyword" ]; then
    echo "Ошибка: укажите файл и ключевое слово"
    return 1
  fi

  # Ищем в логах
  # grep -c это wc -l
  grep -c "$keyword" "$log_file"
}

# Использование
errors=$(parse_logs /var/log/syslog "ERROR")
echo "Найдено ошибок: $errors"