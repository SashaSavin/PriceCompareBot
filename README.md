# PriceCompareBot

**ИНФОРМАЦИЯ**

*HEROKU:* <br>
Название приложения: price-compare-bot <br>
Веб-адресс приложения: https://price-compare-bot.herokuapp.com/ <br>
Procfile: web gunicorn start_heroku:app <br>
GitHub: Igor546/PriceCompareBot <br>

*MongoDB (mLab):* <br>
Cluster: PriceCompareBot <br>
Строка для подключения: mongodb+srv://Admin:<password>@pricecomparebot-mhmiv.mongodb.net/test?retryWrites=true&w=majority <br>

*Github* <br>
https://github.com/Igor546/PriceCompareBot/ <br>

**ЗАПУСК ПРИЛОЖЕНИЯ**
start_heroku.py - Для запуска на Heroku <br>
start_pycharm.py - Для запуска в PyCharm <br>


**ЗАМЕТКИ**
1. Heroku по умолчанию запускает два потока и весь код дублируеться.
РЕШЕНИЕ: В Config Vars добавить переменную WEB_CONCURRENCY = 1
2. Ошибка pymongo.errors.ServerSelectionTimeoutError: connection closed (относиться к внедрению MongoDB)
РЕШЕНИЕ: Возможно проблемы с pymongo (помог ручной Deploy Branch или выждать сутки после регистрации mLab)
