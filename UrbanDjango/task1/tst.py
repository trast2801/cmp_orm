from decimal import Decimal
data =  [{'title': 'DOTA 2', 'description': 'стрелялка', 'cost': Decimal('5000.00')},
{'title': 'world of warcrafy', 'description': 'RPG', 'cost': Decimal('1000.00')},
{'title': 'call of duty', 'description': 'Стрелялка', 'cost': Decimal('3000.00')}]

str =[]
for i in data:
    formatted_string = f"{i['title']}| {i['description']}. Cтоимость: {i['cost']}"
    str.append(formatted_string)
print (str)



data = {'title': 'call of duty', 'description': 'Стрелялка', 'cost': Decimal('3000.00')}

# Форматируем данные в строку
formatted_string = f"{data['title']}: {data['description']}, стоимость: {data['cost']}"

# Выводим результат
print(formatted_string)
'''
from decimal import Decimal
from models import Game

def read_from_games():
    #a = Game.objects.values('title','description', 'cost')
    a =  [{'title': 'DOTA 2', 'description': 'стрелялка', 'cost': Decimal('5000.00')}, {'title': 'world of warcrafy', 'description': 'RPG', 'cost': Decimal('1000.00')}, {'title': 'call of duty', 'description': 'Стрелялка', 'cost': Decimal('3000.00')}]

    lst = []
    for i in a:
        formatted_string = f"{i['title']}: {i['description']}, стоимость: {i['cost']}"
        print (formatted_string)'''