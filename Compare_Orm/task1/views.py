import csv
from os import path
from django.db.models import Count
from django.shortcuts import render
import time
from django.db import connection
from django.template.defaulttags import register
from django.utils import asyncio
from task1.models import *
from task1.sqlalchem_view import *
from tortoise import run_async

from .sqlalchem_view import sql_alchem
from .tortoise_view import tortoise_main


def productivity(request):
    title = "Тестирование производительности"
    head = "Сравнительная таблица"
    data = {}
    perf = Perfomance('Django')
    # exec(open('task1//totrtoise_.py').read())

    # rez = perf.import_from_csv()
    # data['Загрузка тестовых данных']= [[rez, 2, 3 ]]

    # one = perf.import_review()
    # post_count = perf.get_count(request)

    data = calculation_of_indicators(data, perf).copy()
    data = sql_alchem(data).copy()
    #data = asyncio.run(tortoise_main(data)).copy()



    with open('task1//dict.txt', encoding='cp1251') as inp:
        i = str(inp.readlines())

    array = i.split(',')
    z = 0
    for key, j in data.items():
        data.get(key)[0][2] = str(array[z]).replace('[', '')
        z += 1

    context = {
        'title': title,
        'head': head,
        'data': data,

    }
    return render(request, 'productivity.html', context)


from .models import *


# функция тестирования CRUD
def calculation_of_indicators(data: dict, perf):
    rez = perf.simple_query()
    data['Простой запрос к таблице есть запись'] = [[rez, 2, 3]]

    rez = perf.simple_query_not_find_record()
    data['Простой запрос к таблице нет записи'] = [[rez, 2, 3]]

    rez = perf.group_by()
    data['Запрос с GROUP BY'] = [[rez, 2, 3]]

    rez = perf.sort_()
    data['Запрос с сортировкой'] = [[rez, 2, 3]]

    rez = perf.count_filter()
    data['Запрос с условием фильтрации'] = [[rez, 2, 3]]

    rez = perf.join_()
    data['Запрос с JOIN'] = [[rez, 2, 6]]

    rez = perf.add_record()
    data['Добавить запись'] = [[rez, 2, 6]]

    rez = perf.update_records()
    data['Обновление по фильтру'] = [[rez, 2, 6]]

    # rez = perf.del_all_data()
    # data['Удаление тестовых данных']= [[rez, 2, 3 ]]

    return data


class Perfomance():
    def __init__(self, name_):
        self.name_ = name_

    def __str__(self):
        return self.name_

    def import_from_csv(self):
        csv_path = 'data/kp_all_movies_50000.csv'
        model_name = 'Cinema'
        if path.exists(csv_path):
            start = time.time()
            with open(csv_path, encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Cinema.objects.create(
                        name=row['name'],
                        movie_duration=row['movie_duration'],
                        movie_year=row['movie_year'],
                        genres=row['genres'],
                        countries=row['countries'],
                    )
            end = time.time()
            return (f"{(end - start):.3f} сек.")
        else:
            return (f" тестового  файла для загрузки/n не существует по пути: {csv_path}")

    def import_review(self):
        csv_path = 'data/posts.csv'
        if path.exists(csv_path):
            start = time.time()
            with open(csv_path, encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Review.objects.create(
                        name=row['name'],
                        review=row['post'],
                    )
            end = time.time()
            return (f"{(end - start):.3f} сек.")
        else:
            return (f" тестового  файла для загрузки/n не существует по пути: {csv_path}")

    def del_all_data(self):
        start = time.time()
        Cinema.objects.all().delete()
        end = time.time()
        return (f"{(end - start):.3f} сек.")

    def simple_query(self):
        start = time.time()
        Cinema.objects.get(name='Исход')

        end = time.time()
        return (f"{(end - start):.3f} сек.")

    def simple_query_not_find_record(self):
        start = time.time()
        Cinema.objects.filter(name="value").first()
        end = time.time()
        return (f"{(end - start):.3f} сек.")

    @register.simple_tag
    def get_count(self, request):
        post_count = '{Review.objects.all().count()}'
        print(f'post_count')
        return render(request, 'productivity.html', {'post_count': post_count})

    def group_by(self):
        start = time.time()
        Cinema.objects.values('movie_year').annotate(total_posts=Count('movie_year')).order_by('movie_year')

        end = time.time()
        return (f"{(end - start):.3f} сек.")

    def sort_(self):
        start = time.time()
        Cinema.objects.all().order_by('name')
        end = time.time()
        return (f"{(end - start):.3f} сек.")

    def join_(self):
        start = time.time()
        with connection.cursor() as cursor:
            cursor.execute("""
                    Select task1_cinema.name, task1_review.review from task1_cinema JOIN task1_review ON
                     task1_cinema.name = task1_review.name
                """)
        # Django не может связать таблицы где нет явно указанной связи
        end = time.time()
        return (f"{(end - start):.3f} сек.")

    def count_filter(self):
        start = time.time()
        Cinema.objects.all().filter(countries='[США]').aggregate(Count('countries'))
        end = time.time()
        return (f"{(end - start):.3f} сек.")

    def add_record(self):
        start = time.time()
        a = Cinema.objects.create(name="test", movie_duration="test")
        a.save()
        end = time.time()
        return (f"{(end - start):.3f} сек.")

    def update_records(self):
        start = time.time()
        query_for_filter = Cinema.objects.filter(countries='test Updated')
        query_for_filter.update(countries=('test') + ' Updated')
        # query_for_filter.save()
        end = time.time()
        return (f"{(end - start):.3f} сек.")
