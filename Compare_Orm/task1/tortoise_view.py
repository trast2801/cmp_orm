import os
import time

from tortoise import Tortoise, fields, models, run_async
from tortoise.functions import Count
from task1.T_models.T_Cinema_ import T_Cinema
from task1.T_models.T_Review_ import T_Review

DB_PATH = r"/Compare_Orm\db.sqlite3"


async def tortoise_init():
    db_file_path = os.path.join(os.getcwd(), 'db.sqlite3')
    await Tortoise.init(
        db_url="sqlite:///C:\\python_django2\\19module\\Compare_Orm\\db.sqlite3",
        #db_url="sqlite:///" + db_file_path,
        modules={'models': ['T_models.T_Cinema_', 'T_models.T_Review_']},
    )
    await Tortoise.generate_schemas()


async def t_simple_query(data: dict, find_yes: bool):
    start = time.time()
    if find_yes:
        review = await T_Cinema.filter(countries='[США]').first()
        end = time.time()
        data['Простой запрос к таблице есть запись'][0][2] = f"{(end - start):.3f} сек."
    else:
        review = await T_Cinema.filter(countries='[ХХХ]').first()
        end = time.time()
        data['Простой запрос к таблице нет записи'][0][2] = f"{(end - start):.3f} сек."


async def t_group_by(data: dict):
    start = time.time()
    review = await T_Cinema.annotate(count=Count("movie_year")).group_by("movie_year").all()
    end = time.time()
    data['Запрос с GROUP BY'][0][2] = f"{(end - start):.3f} сек."


async def t_sort(data: dict):
    start = time.time()
    review = await T_Cinema.all().order_by("countries")
    end = time.time()
    data['Запрос с сортировкой'][0][2] = f"{(end - start):.3f} сек."


async def t_filter(data: dict):
    start = time.time()
    review = await T_Cinema.filter(countries='[США]').all()
    end = time.time()
    data['Запрос с условием фильтрации'][0][2] = f"{(end - start):.3f} сек."


async def t_join(data: dict):
    start = time.time()
    conn = Tortoise.get_connection("default")
    reviews = await conn.execute_query_dict("Select task1_cinema.name, task1_review.review from task1_cinema "
                                            "JOIN task1_review ON task1_cinema.name = task1_review.name")
    end = time.time()
    data['Запрос с JOIN'][0][2] = f"{(end - start):.3f} сек."


async def t_add_record(data: dict):
    start = time.time()
    # Добавляем условие чтобы установить 'cinema'
    some_cinema = await T_Cinema.first()
    review = await T_Review.create(review="ccccccccccccccccccccccccccccccccccccccccccccccccc", name="что-то такое",
                                   cinema=some_cinema)
    end = time.time()
    data['Добавить запись'][0][2] = f"{(end - start):.3f} сек."


async def t_update_records(data: dict):
    start = time.time()
    await T_Cinema.filter(countries='test Updated').update(countries='TEST')
    end = time.time()
    data['Обновление по фильтру'][0][2] = f"{(end - start):.3f} сек."


async def tortoise_main(data: dict):
    data = {
        'Простой запрос к таблице есть запись': [["", "", ""]],
        'Простой запрос к таблице нет записи': [["", "", ""]],
        'Запрос с GROUP BY': [["", "", ""]],
        'Запрос с сортировкой': [["", "", ""]],
        'Запрос с условием фильтрации': [["", "", ""]],
        'Запрос с JOIN': [["", "", ""]],
        'Добавить запись': [["", "", ""]],
        'Обновление по фильтру': [["", "", ""]]
    }
    await tortoise_init()
    await t_simple_query(data, True)
    await t_simple_query(data, False)
    await t_group_by(data)
    await t_sort(data)
    await t_filter(data)
    await t_join(data)
    await t_add_record(data)
    await t_update_records(data)
    await Tortoise.close_connections()
    return data

'''
if __name__ == "__main__":
    data = {
        'Простой запрос к таблице есть запись': [["", "", ""]],
        'Простой запрос к таблице нет записи': [["", "", ""]],
        'Запрос с GROUP BY': [["", "", ""]],
        'Запрос с сортировкой': [["", "", ""]],
        'Запрос с условием фильтрации': [["", "", ""]],
        'Запрос с JOIN': [["", "", ""]],
        'Добавить запись': [["", "", ""]],
        'Обновление по фильтру': [["", "", ""]]
    }
    run_async(tortoise_main(data))

    nev = ""

    for i, j in data.items():
        nev = nev + (j[0][2]) + ','
        print(i, j)
    file_path = os.path.join(os.getcwd(), 'dict.txt')
    #with open(r'Compare_Orm\task1\dict.txt', 'w') as i:
    with open(file_path, 'w', encoding='cp1251') as i:
        i.write(str(nev))
'''