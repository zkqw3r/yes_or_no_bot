# Инструкция по деплою на сервер

## 1. Подготовка на сервере

```bash
# Клонируй репозиторий
git clone <your-repo-url>
cd yes_or_no_bot

# Создай виртуальное окружение
python3 -m venv ../venv
source ../venv/bin/activate

# Установи зависимости
pip install aiogram aiohttp

# Создай .env файл с токеном
nano settings/.env
# Добавь: TELEGRAM_TOKEN=your_bot_token_here
```

## 2. Настройка systemd (чтобы бот не отрубался)

```bash
# Отредактируй файл reshala-bot.service
nano reshala-bot.service

# Замени:
# YOUR_USERNAME -> твой юзер на сервере (например: ubuntu, root)
# /path/to/yes_or_no_bot -> полный путь к папке (например: /home/ubuntu/yes_or_no_bot)
# /path/to/venv -> полный путь к venv (например: /home/ubuntu/venv)

# Скопируй service файл
sudo cp reshala-bot.service /etc/systemd/system/

# Перезагрузи systemd
sudo systemctl daemon-reload

# Включи автозапуск
sudo systemctl enable reshala-bot

# Запусти бота
sudo systemctl start reshala-bot

# Проверь статус
sudo systemctl status reshala-bot
```

## 3. Полезные команды

```bash
# Посмотреть логи
sudo journalctl -u reshala-bot -f

# Перезапустить бота
sudo systemctl restart reshala-bot

# Остановить бота
sudo systemctl stop reshala-bot

# Проверить статус
sudo systemctl status reshala-bot
```

## 4. Альтернатива: screen (проще, но менее надежно)

```bash
# Установи screen
sudo apt install screen

# Запусти бота в screen
screen -S bot
cd yes_or_no_bot
source ../venv/bin/activate
python -m telegram.bot

# Отключись: Ctrl+A, потом D

# Вернуться к боту
screen -r bot
```

## 5. Обновление бота

```bash
cd yes_or_no_bot
chmod +x deploy.sh
./deploy.sh
```
