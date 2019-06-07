import requests
import json
import datetime
from termcolor import cprint
from time import sleep

# Класс бота, который работает через API Telegram (Flask, Webhook)
class BotWebhook:
    # И Н Ф О Р М А Ц И Я
    # Получать обновления от телеграм можно через: 1) getupdates 2) Webhook
    #    1) Если "getupdates" - то работаем просто через [requests.post / requests.get]
    #    2) Если "Webhook"    - то работаем через [Django / Flask]
    # Работать с Flask можно через: 1) localhost 2) Тунель HTTP (localhost.run) 3) Тунель HTTPS (ngrok.com) 4) Хостинг

    # А Т Р И Б У Т Ы
    JSON = None  # Ответ от бота в JSON формате (все сообщения пользователя)
    COLOR = 'yellow'

    # Инициализаци/создание бота
    # https://api.telegram.org/bot888175405:AAGnCJ-dGyToTh3lGaa-D716cjLKtZVTgAk/setWebhook?url=https://lawr.localhost.run/
    def __init__(self, token, web_address):
        self.TOKEN = token
        self.URL = "https://api.telegram.org/bot" + token + "/"
        requests.get(url=self.URL + 'setWebhook?url=' + web_address)
        print()
        cprint(self.time() + " ClassLawr_BotWebhook Инициализация бота (Установка Webhook: {})".format(web_address),
               self.COLOR, attrs=['bold'])

    # ЗАПИСАТЬ JSON В ФАЙЛ (с форматирование)
    @staticmethod
    def write_json(myjson, filename):
        # Создаем object_filename(открытый для записи файловый объект) привязанный к файлу "filename"
        with open(filename, 'w') as file:
            # Метод который записывает в object_filename(файловый объект) данные JSON
            json.dump(myjson, file, indent=2, ensure_ascii=False)

    # ПОЛУЧАТЬ Сообщения
    def get_message(self):
        # Вытягивем из JSON данные относящиеся к сообщению
        update_id = self.JSON['update_id']
        try:
            chat_id = self.JSON['message']['chat']['id']
            date = self.JSON['message']['date']
            text = self.JSON['message']['text']
        except KeyError:
            chat_id = self.JSON['edited_message']['chat']['id']
            date = self.JSON['edited_message']['date']
            text = self.JSON['edited_message']['text']
        # Формируем словарь на основе вытянутых данных
        MESSAGE_INCOMING = {'chat_id': chat_id, 'update_id': update_id, 'date': date, 'text': text}
        print()
        cprint(self.time() + " ClassLawr_BotWebhook get_message {}".format(MESSAGE_INCOMING),
               self.COLOR, attrs=['bold'])
        sleep(2)
        return MESSAGE_INCOMING

    # ОТПРАВЛЯТЬ Сообщения
    def send_message(self, chat_id, text, methods="POST", parse_mode=None):
        MESSAGE_SENT = None
        if methods == "POST":
            MESSAGE_SENT = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode}
            requests.post(self.URL + 'sendmessage', json=MESSAGE_SENT)
        if methods == "GET":
            requests.get(self.URL + 'sendmessage?chat_id={}&text={}&parse_mode={}'.format(chat_id, text, parse_mode))
        cprint(self.time() + " ClassLawr_BotWebhook send_message", self.COLOR, attrs=['bold'])

    # Быстрая отправка сообщения
    def fast_send(self, text, parse_mode=None):
        MESSAGE_INCOMING = self.get_message()
        self.send_message(MESSAGE_INCOMING['chat_id'], text=text, parse_mode=parse_mode)

    # Возвращает текущее время
    @staticmethod
    def time():
        return datetime.datetime.today().strftime("[%H:%M:%S]")

    # Возвращает табуляцию равную длинне символов времене
    @staticmethod
    def tb():
        return "          "
