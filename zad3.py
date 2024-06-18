# 3. Запросите у пользователя идентификатор аккаунта VK, у которого 
# он желает просмотреть список друзей. Выведите только общее количество
#  друзей пользователя в консоль. Для этого Вам необходимо, как и при работе
#  с любым API, найти необходимый метод и изучить его описание, параметры 
# и их значения, которыми можно варьировать. Также для работы с API VK Вам
#  потребуется access token, процедуру получения которого мы разбирали на практике.
#  Используйте API VK https://dev.vk.com/ru/method

# * По желанию доработайте программу: выведите основную информацию о каждом друге 
# и дополнительно информацию о последнем его заходе в сеть. В полученном json 
# друзья сразу должны быть отсортированы имени. 


from vk_api import VkApi  # можно через модули API VK
from vk_api.exceptions import ApiError
import requests  # можно через модуль запроса по URL через метод GET
import json  # используем модуль работы с объектами json
import time

BASE_URL = 'https://api.vk.com'  # адрес, откуда будем брать данные

# Ваш токен доступа
token = 'c0225b76c0225b76c0225b76cec05e58f7cc022c0225b76a26e5dc3bde7de64686b6751'

# ID пользователя, чей список друзей мы хотим получить
target_user_id = input("Введите id пользователя ВКонтакте ")
# target_user_id = ''


# **************************************
# обмен данными через Через объект VKApi
# **************************************

# Создаем объект VKSession
vk_session = VkApi(token=token, )

# Получаем объект VK_API
vk = vk_session.get_api()

try:
    # Получение списка друзей пользователя
    friends = vk.friends.get(user_id=target_user_id)
    print("Всего друзей ", friends['count'])  # вывод только количества
    
    # Вывод списка друзей
    print(f"Список друзей пользователя с ID {target_user_id}:")
   # for friend_id in friends['items']:
    #    friend_info = vk.users.get(user_ids=friend_id, fields='first_name,last_name')
    #    print(friend_info[0]['first_name'], friend_info[0]['last_name'], friend_info[0])

except ApiError as e:  # обработка исключений при запросе
    print(f"Ошибка VK API: {e}")


# **************************************
# Обмен данными через request
# **************************************

# Задаем параметры - ищем друзей пользовтеля, порядок сортироваки - по имени
# кол-во - не более 1000, ищем поле last_seen - последний вход
# задаем свой токен, иначе не пустят и версию API
member_request_params = (
        ('user_id', int(target_user_id)),
        ('order', 'name'),
        ('count', 1000),
        ('fields', 'last_seen'),
        ('access_token', token),
        ('v', '5.119'))

# Запрашиваем данные через метод GET VK и переводим в текст
r = requests.get(f"{BASE_URL}/method/friends.get", params=member_request_params).text
# загружаем ответ в переменную-словарь
r1 = json.loads(r)
 
# Примитивный парсинг json
# полученный словарь проходим в цикле, выявляя название и значение строки
for k, v in r1.items(): 
    v1=v['items'] # берем вторую колонку, это list
    #print(v)
    for k1 in v1:  # смотрим список по каждому элементу
        #print(k1)
        print("\n") # эстетический интервал на печать
        for k2, v2 in k1.items():  # элементы списка - словари, идем по словарю
            #print(k2,type(v2))
            if k2=='id':  # нашли поле id? выведем его значение
                print("id=",v2, end=" ")
            elif k2=='first_name': # нашли поле имя? выведем его значение
                print("Имя=",v2, end=" ")
            elif k2=='last_name': # нашли поле фамилия? выведем его значение
                print("Фамилия=",v2, end=" ")
            elif k2=='last_seen': # нашли поле последний вход? цикл по вложенному словарю
                for k3, v3 in v2.items(): 
                    #print(k3,v3)
                    if k3=='time': # нашли переменную время? выведем
                        my_time=time.ctime(v3)  # зададим формат вывода времени
                        print("Последний вход=",my_time, end=" ")

print('\n\nThats all Folks!')