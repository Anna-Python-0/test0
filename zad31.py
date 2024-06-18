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


from vk_api import VkApi
from vk_api.exceptions import ApiError
import requests  # используем модуль запроса по URL через метод GET
import json  # используем модуль работы с объектами json
import time

BASE_URL = 'https://api.vk.com'  # адрес, откуда будем брать данные

# Ваш токен доступа
token = 'c0225b76c0225b76c0225b76cec05e58f7cc022c0225b76a26e5dc3bde7de64686b6751'

# ID пользователя, чей список друзей мы хотим получить
target_user_id = '58970296'


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

except ApiError as e:
    print(f"Ошибка VK API: {e}")


# **************************************
# Обмен данными через request
# **************************************

member_request_params = (
        ('user_id', target_user_id),
        ('order', 'name'),
        ('count', 1000),
        ('fields', 'last_seen'),
        ('access_token', token),
        ('v', '5.119'))
r = requests.get(f"{BASE_URL}/method/friends.get", params=member_request_params).text
r1 = json.loads(r)
 
for k, v in r1.items(): 
    v1=v['items']
    #print(v)
    for k1 in v1: 
        #print(k1)
        print("\n")
        for k2, v2 in k1.items(): 
            #print(k2,type(v2))
            if k2=='id':
                print("id=",v2, end=" ")
            elif k2=='first_name':
                print("Имя=",v2, end=" ")
            elif k2=='last_name':
                print("Фамилия=",v2, end=" ")
            elif k2=='last_seen':
                for k3, v3 in v2.items(): 
                    #print(k3,v3)
                    if k3=='time':
                        my_time=time.ctime(v3)
                        print("Последний вход=",my_time, end=" ")








#domain = "https://api.vk.com/method"

#query_params = {
#    'domain' : domain,
#    'access_token': token,
#    'user_id': target_user_id
#}

#for friend_id in friends['items']:
 #   print(i)
 #   query = "{domain}/users.get?access_token={access_token}&user_id={friend_id}&v=5.119".format(**query_params)
    #response = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=20&mode=2&version=2'.format(server=data['server'], key=data['key'], ts=data['ts'])).json()  
    # отправление запроса на Long Poll сервер со временем ожидания 20 и опциями ответа 2


#query = "{domain}/users.get?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.119".format(**query_params)
#response = requests.get(query)

# сохраняем строкутуру json в переменной
#data = response.json()
#print(json.dumps(data,indent=2))

# Use the json module to load CKAN's response into a dictionary.
#response_dict = json.loads(response.text)

#print(response_dict)
#for i in response_dict:
#    print("key: ", i, "val: ", response_dict[i])



# часть кода в этом примере опущена для сокращения места, без нее код работать не будет
#while True:
#    response = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=20&mode=2&version=2'.format(server=data['server'], key=data['key'], ts=data['ts'])).json()  # отправление запроса на Long Poll сервер со временем ожидания 20 и опциями ответа 2
#    updates = response['updates']
#    if updates:  # проверка, были ли обновления
##        for element in updates:  # проход по всем обновлениям в ответе
 #           action_code = element[0]  # запись в переменную кода события
 #           if action_code == 80:  # проверка кода события
 ##               print('количество непрочитанных сообщений стало равно', element[1])  # вывод
 #   data['ts'] = response['ts']  # обновление номера последнего обновления


#user_id = element[1] * -1  # id пользователя, ставшего оффлайн
#user = requests.get('https://api.vk.com/method/users.get', params={'user_ids': user_id, 'fields': 'sex'}).json()['response'][0]  # имя, фамилия и пол пользователя с id = user_id 
#timeout = bool(element[2])  # был ли поставлен статус оффлайн по истечении тайм-аута

#last_visit = element[3]  # время последнего действия пользователя на сайте в Unix time
#time.ctime(last_visit).split()[3]

