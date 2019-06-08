# PriceCompareBot

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
- start_heroku.py - Для запуска на Heroku <br>
- start_pycharm.py - Для запуска в PyCharm <br>


# ЗАМЕТКИ
- Heroku по умолчанию запускает два потока и весь код дублируеться. РЕШЕНИЕ: В Config Vars добавить переменную WEB_CONCURRENCY = 1
- Ошибка pymongo.errors.ServerSelectionTimeoutError: connection closed (относиться к внедрению MongoDB) РЕШЕНИЕ: Возможно проблемы с pymongo (помог ручной Deploy Branch или выждать сутки после регистрации mLab)
