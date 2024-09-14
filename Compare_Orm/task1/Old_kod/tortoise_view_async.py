import time

import tortoise
from tortoise import Tortoise, fields, models, run_async
from tortoise.models import Model
from tortoise import fields

from task1.T_models import T_Cinema


#from task1.models_tortoise import *

#from task1.models_tortoise import T_Cinema
async def tortoise_main(data: dict):
    await Tortoise.init(
        db_url="sqlite:///C:\\python_django2\\19module\\Compare_Orm\\db.sqlite3",
        modules={"models": ["task1.T_models"]},
    )
    await Tortoise.generate_schemas()

    task = await T_Cinema.filter(countries='[США]').first()

    data['Обновление по фильтру'] = [[1000, 2, 'rrrr']]
    await Tortoise.close_connections()
    return data
'''
async def tortoise_main(data: dict):
    path_models = "./models"

    await Tortoise.init(
        #db_url="sqlite://db.sqlite3",
        db_url="sqlite:///C:\\python_django2\\19module\\Compare_Orm\\db.sqlite3",
        modules={"models": ["task1.T_models"]},
    )
    #Tortoise.init_models([ "task1.T_models.T_Cinema"], "models")
    await Tortoise.generate_schemas()

    #task = await T_Cinema.filter(countries='[США]').first()
    task = T_Cinema.filter(countries = '[США]')

    #rez = await al_simple_query(True)
    data['Обновление по фильтру'] = [[1000, 2, 'rrrr']]
    await Tortoise.close_connections()
    return data
    
    await Tortoise.generate_schemas()


    rez = await al_simple_query(True)
    #data['Простой запрос к таблице есть запись[[[[['][0][2] = 11000000
    data['Простой запрос ['] = [[1000, 2, 6]]
    # print (data['Простой запрос к таблице есть записьхххххх'][0][2])
'''


#if __name__ == "__main__":
#    run_async(tortoise_main())

async def al_simple_query(find_yes : bool):
    start = time.time()
    if find_yes :
        # получение первого из всех объектов
        task = await T_Cinema.filter(countries='[США]').first()
    else:
        task = await T_Cinema.filter(countries = '[ХХХ]').first()
        if task == None:
            print("Запись не найдена")
    end = time.time()
    return (f"{(end - start):.3f} сек.")