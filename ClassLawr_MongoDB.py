import pymongo
import ssl


# Класс для работы с БД "MongoDB"
class MongoDB:
    # Инициализаци/открытие БД
    def __init__(self, connection_string, ssl):
        if ssl:
            self.CLIENT = pymongo.MongoClient(connection_string, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
        else:
            self.CLIENT = pymongo.MongoClient(connection_string)

        print("-> Подключение к БД ({})".format(self.CLIENT))

    # Возвращает True если коллекция существует
    def check_collection(self, dbs, name_collection):
        for collection in self.show_database(dbs):
            if collection == name_collection:
                return True
        return False

    # Удаление коллекции
    def delete_collection(self, dbs, collection):
        self.CLIENT[dbs][collection].drop()
        print("-> [{}.{}] Коллекция удалена".format(dbs, collection))

    # Очистка всех документов в коллекции
    def clear_collection(self, dbs, collection):
        self.CLIENT[dbs][collection].remove({})
        print("-> [{}.{}] Коллекция очищена".format(dbs, collection))

    # Выводит СПИСОК, каждый элемент это СЛОВАРЬ (документ из коллекции), в СЛОВАРЕ элементы (ячейки документа)
    def show_collection(self, dbs, collection):
        result = []
        coll = self.CLIENT[dbs][collection]
        for documet in coll.find():
            result.append(documet)
        return result

    # Выводит СПИСОК, каждый элемент это ИМЯ коллекции
    def show_database(self, dbs):
        return self.CLIENT[dbs].collection_names()

    # Красивая печать РЕЗУЛЬАТОВ полученных при помощи функций "show_.."
    @staticmethod
    def nice_print(result):
        print("-> nice_print:")
        for documet in result:
            print('     ', documet)

    # Добавление строки "value" в конец коллекции "collection" в БД "dbs"
    def add_line_to_end(self, dbs, collection, value):
        coll = self.CLIENT[dbs][collection]
        coll.save(value)
        print("-> [{}.{}] Добавлен документ в конец".format(dbs, collection))

    # Удаление документа в конеце коллекции
    def del_line_to_end(self, dbs, collection):
        coll = self.CLIENT[dbs][collection]
        temp = self.show_collection(dbs, collection)[-1]
        coll.remove(temp, True)
        print("-> [{}.{}] Удален документ в конце".format(dbs, collection))
