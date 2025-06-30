import requests

from config.settings import TOKEN_BOT


def send_message(message, chat_id):
    ''' Функция для сообщения в Телеграмм '''

    params = {
        "text": message,
        "chat_id": chat_id,
    }

    requests.get(f"https://api.telegram.org/bot{TOKEN_BOT}/sendMessage", params=params)
