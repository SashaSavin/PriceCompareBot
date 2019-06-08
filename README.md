# PriceCompareBot
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
# ИНФОРМАЦИЯ
**HEROKU:**
- Название приложения: price-compare-bot
- Веб-адресс приложения: https://price-compare-bot.herokuapp.com/
- Procfile: web gunicorn start_heroku:app
- GitHub: Igor546/PriceCompareBot

**MongoDB (mLab):**
- Cluster: PriceCompareBot
- Строка для подключения: mongodb+srv://Admin:<password>@pricecomparebot-mhmiv.mongodb.net/test?retryWrites=true&w=majority

**Github**
- https://github.com/Igor546/PriceCompareBot/ <br>

# ЗАПУСК ПРИЛОЖЕНИЯ
- **start_heroku.py** - Для запуска на Heroku
*Ничего не нужно, все уже работает и настроенно.* 
Logs: "heroku logs --tail --app price-compare-bot"
Deploy/Restart: Automatic deploys from  master
- **start_pycharm.py** - Для запуска в PyCharm
*Для работы бота нужен запуск Flask, с нормальным веб адрессом, поэтому рекомендую использовать тунель Ngrock.*

> Следует учитывать что призапуске из PyCharm, Heroku не останавливается и все взаимодействия будут в двух потоках. При debug чтобы не поломать БД и TG Bot просите отключить сервер, или проводите все тесты на тестовой своей БД и Token Bot.


# ЗАМЕТКИ
- Heroku по умолчанию запускает два потока и весь код дублируеться. РЕШЕНИЕ: В Config Vars добавить переменную WEB_CONCURRENCY = 1
- Ошибка pymongo.errors.ServerSelectionTimeoutError: connection closed (относиться к внедрению MongoDB) РЕШЕНИЕ: Возможно проблемы с pymongo (помог ручной Deploy Branch или выждать сутки после регистрации mLab)
