# 2. Выведите информацию о всех корзинах пользователей (Cart), представленных 
# на https://fakestoreapi.com. Проанализируйте данные и устно ответьте на вопрос,
#  что из себя представляют эти корзины и какая информация в них находится - что 
# означает каждое поле в полученном json.

#* По желанию доработайте программу: запросите у пользователя его имя 
# (или идентификатор), в соответствии с этим выведите содержание всех корзин
# этого пользователя в отформатированном для чтения виде в консоль. 
# Используйте API https://fakestoreapi.com/docs.


import requests  # используем модуль запроса по URL через метод GET
import json  # используем модуль работы с объектами json

BASE_URL = 'https://fakestoreapi.com'  # адрес, откуда будем брать данные

# запросим данные по методу GET с базового адреса + путь, который оттуда вернет данные корзин всех пользователй
response = requests.get(f"{BASE_URL}/carts")  
print(json.dumps(response.json(), indent=2))  # вывод результата - список корзин


# Анализ структуры корзины покупателя 
#  [
#            {
#                id:5,  # номер корзины
#                userId:2,  # ID покупателя
#                date:2019-10-03,  #  дата покупки
#                products:[...]  # какие продукты куплены
#            },
#   ]

# запросим пользователя выбрать нужного покупателя
num = int(input("Введите ID пользователя: "))

# Выберем товары из введенной категории
try:  # начало попытки выбора
    # запрашиваем корзину по номеру покупателя
    response = requests.get(f"{BASE_URL}/carts/user/{num}")
    # сохраняем строкутуру json в переменной
    data = response.json()

    print("Корзина выбранного пользователя:\n")
    print(json.dumps(data, indent=2)) # выводим данные json в форматном виде
except Exception:  # если проиозшло исключение при поиске корзины покупателя
    print('Похоже нет такой категории)')