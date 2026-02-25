#!/bin/bash

is_even() {
  local number=$1  # Локальная переменная
  if (( number % 2 == 0 )); then
    echo "Чётное"
    return 0  # Успех
  else
    echo "Нечётное"
    return 1  # Ошибка
  fi
}

# Использование
result=$(is_even 4)
echo "$result"  # Выведет "Чётное"