echo "=== Деплой Reshala Bot ==="

echo "Обновляем код..."
git pull

echo "Устанавливаем зависимости..."
source ../venv/bin/activates
pip install -q aiogram aiohttp

if [ ! -f "settings/.env" ]; then
    echo "ОШИБКА: Файл settings/.env не найден!"
    echo "Создай его и добавь TELEGRAM_TOKEN=your_token"
    exit 1
fi

if systemctl is-active --quiet reshala-bot; then
    echo "Перезапускаем сервис..."
    sudo systemctl restart reshala-bot
    echo "Статус сервиса:"
    sudo systemctl status reshala-bot --no-pager
else
    echo "Сервис не настроен. Запускаем вручную..."
    python -m telegram.bot
fi
