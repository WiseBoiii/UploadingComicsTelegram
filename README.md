# Парсинг комиксов XKCD и отправка их в Telegram

**xkcd_telegram_bot** — это скрипт на Python, который автоматически скачивает последний комикс с сайта [XKCD](https://xkcd.com/) и отправляет его в указанный Telegram-канал.

## Требования

Перед использованием убедитесь, что у вас установлены следующие компоненты:

- **Python 3.11** или выше.
- Библиотеки, указанные в файле `requirements.txt`.

## Установка

1. **Клонируйте репозиторий:**

   ```bash
     git clone https://github.com/ваш_пользователь/xkcd_telegram_bot.git
     cd xkcd_telegram_bot
   ```

2. **Создайте и активируйте виртуальное окружение:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
    ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте переменные окружения:**
  Создайте файл .env в корне проекта и добавьте следующие строки:
    ```bash
    BOT_TOKEN=ваш_токен_бота
    CHAT_ID=ваш_id_канала
    ```

## Запуск скрипта и результат

**Запуск скрипта:**
  ```bash
  python download_comics.py
  python telegran.py
  ```

После выполнения вы увидете, что в вашем канале появился XKCD комикс!

![Пример результата в тестовом телеграм канале](https://github.com/WiseBoiii/UploadingComicsTelegram/blob/main/Example%20of%20result.png)

![alt text](https://github.com/WiseBoiii/TelegramPictureLoader/blob/main/nice.gif)
