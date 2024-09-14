import asyncio
import time

import tortoise
from tortoise import Tortoise, fields, models, run_async

from task1.models_tortoise import *

data12 = {
            'Обновление по фильтру'  : [[1000, 2, 6]],
            'Обновление по фильтру2' : [[1000, 2, 6]],
        }
async  def tortoise_main(data1: dict):
        data1['Обновление по фильтру2'] = [[1000, 2, 10000]]
        return data1

'''
    Tortoise.init(
        #db_url="sqlite://db.sqlite3",
        db_url="sqlite:///C:\\python_django2\\19module\\Compare_Orm\\db.sqlite3",

        # Модулем для моделей указываем __main__,
        # т.к. все модели для показа будем прописывать
        # именно тут
        # modules={'models': ['__main__']},
    )
    Tortoise.generate_schemas()

    rez =  al_simple_query(True)
    data['Простой запрос к таблице есть запись'][0][2] =  rez
    #print (data['Простой запрос к таблице есть запись'][0][2])
    for i in data.item():
        print (i)
    Tortoise.close_connections()
    return  data




def al_simple_query(find_yes : bool):
    start = time.time()
    if find_yes :
        # получение первого из всех объектов
        task =  T_Cinema.objects.filter(countries='[США]').first()
    else:
        task =  T_Cinema.objects.filter(countries = '[ХХХ]').first()
        if task == None:
            print("Запись не найдена")
    end = time.time()
    return (f"{(end - start):.3f} сек.")

'''