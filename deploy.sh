#!/bin/bash

# Скрипт для деплоя бота на сервер

echo "=== Деплой Reshala Bot ==="

# 1. Обновляем код
echo "Обновляем код..."
git pull

# 2. Активируем venv и устанавливаем зависимости
echo "Устанавливаем зависимости..."
source ../venv/bin/activate
pip install -q aiogram aiohttp

# 3. Проверяем .env
if [ ! -f "settings/.env" ]; then
    echo "ОШИБКА: Файл settings/.env не найден!"
    echo "Создай его и добавь TELEGRAM_TOKEN=your_token"
    exit 1
fi

# 4. Перезапускаем systemd service (если настроен)
if systemctl is-active --quiet reshala-bot; then
    echo "Перезапускаем сервис..."
    sudo systemctl restart reshala-bot
    echo "Статус сервиса:"
    sudo systemctl status reshala-bot --no-pager
else
    echo "Сервис не настроен. Запускаем вручную..."
    python3 -m telegram.bot
fi
