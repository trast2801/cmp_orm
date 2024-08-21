import csv
from os import path

from django.contrib.sites import management
from django.db.models import Count
from django.shortcuts import render
import time
from django.db import connection
from django.template.defaulttags import register
from django.test import TestCase
from psycopg2._psycopg import cursor
from task1.models import *
# Create your views here.

def productivity(request):
    title = "Тестирование производительности"
    head = "Сравнительная таблица"

    data = {}
    perf = Perfomance('Django')

    #rez = perf.import_from_csv()
    #data['Загрузка тестовых данных']= [[rez, 2, 3 ]]

    #one = perf.import_review()
    #post_count = perf.get_count(request)

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
    data['Запрос с JOIN'] = [[rez, 2, 3]]

    #rez = perf.del_all_data()
    data['Удаление тестовых данных']= [[rez, 2, 3 ]]

    context = {
        'title' : title,
        'head': head,
        'data' : data,
        'rez' : rez,
        #'post_count' : post_count,
    }

    return render(request, 'productivity.html', context)



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
            return  (f"{(end - start):.3f} сек.")
        else:
            return  (f" тестового  файла для загрузки/n не существует по пути: {csv_path}")

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
    def get_count(self,request):
         post_count = '{Review.objects.all().count()}'
         return render(request, 'productivity.html', {'post_count': post_count})

    def group_by(self):
        start = time.time()
        Cinema.objects.values('movie_year').annotate(total_posts=Count('movie_year')).order_by('movie_year')
        end = time.time()
        return (f"{(end - start):.3f} сек.")

    def sort_(self):
        start = time.time()
        Cinema.objects.all().order_by('countries')
        end = time.time()
        return (f"{(end - start):.3f} сек.")

    def join_(self):
        start = time.time()
        with connection.cursor() as cursor:
            cursor.execute("""
                    Select task1_cinema.name, task1_review.review from task1_cinema JOIN task1_review ON
                     task1_cinema.name = task1_review.name
                """)
        #Django не может связать таблицы где нет явно указанной связи
        end = time.time()
        return (f"{(end - start):.3f} сек.")

    def count_filter(self):
        start = time.time()
        Cinema.objects.all().filter(countries='[США]').aggregate(Count('countries'))
        end = time.time()
        return (f"{(end - start):.3f} сек.")




'''
class PerformanceTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создание тестовых данных
        cls.create_test_data()

    @classmethod
    def tearDownClass(cls):
        # Удаление тестовых данных
        cls.delete_test_data()
        super().tearDownClass()

    def test_performance_of_complex_queries(self):
        with self.subTest("Query 1"):
            # Запрос 1
            # Путь к CSV файлу
            csv_path = 'data/kp_all_movies.csv'

            # Имя модели, которая будет создана на основе CSV файла
            model_name = 'Cinema'

            # Импорт данных из CSV файла
            start = time.time()
            management.call_command('import_csv', model_name, csv_path)
            #results = Cinema.objects.complex_query_1()
            end = time.time()
            print(f" Время загрузки в БД  1 took {end - start} секунд.")

        with self.subTest("Query 2"):
            # Запрос 2
            start = time.time()
            results = Cinema.objects.complex_query_2()
            end = time.time()
            print(f"Complex query 2 took {end - start} seconds.")


    def create_test_data(self):
        # Функция для создания тестовых данных
    

    def delete_test_data(self):
        # Функция для удаления тестовых данных
'''