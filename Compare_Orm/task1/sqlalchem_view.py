import os
import time

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from task1.models_alchem import *
from sqlalchemy import func
from sqlalchemy.orm import Session

def sql_alchem(data : dict):

    #engine=create_engine('sqlite:///C:\\python_django2\\19module\\Compare_Orm\\db.sqlite3')
    db_file_path = os.path.join(os.getcwd(), 'db.sqlite3')

    # Создание соединения с базой данных
    engine = create_engine('sqlite:///' + db_file_path)
    with Session(autoflush=False, bind=engine) as db:
        rez = al_simple_query(db, True)
        data['Простой запрос к таблице есть запись'][0][1] = rez
        rez = al_simple_query(db, False)
        data['Простой запрос к таблице нет записи'][0][1] = rez
        rez = al_group_by(db)
        data['Запрос с GROUP BY'][0][1] = rez
        rez = al_sort(db)
        data['Запрос с сортировкой'][0][1] = rez
        rez = al_filter(db)
        data['Запрос с условием фильтрации'][0][1] = rez
        rez= al_join(db)
        data['Запрос с JOIN'][0][1] = rez
        rez = al_add_record(db)
        data['Добавить запись'][0][1] = rez
        rez = al_update_records(db)
        data['Обновление по фильтру'][0][1] = rez

    db.close()
    return data

def list_all(db : Session ):
   start = time.time()
   # получение всех объектов
   review = db.query(Review).all()
   for p in review:
       print(f"{p.id}.{p.name}")
   end = time.time()
   return (f"{(end - start):.3f} сек.")

def al_simple_query(db: Session, find_yes : bool):
    start = time.time()
    if find_yes :
    # получение первого из всех объектов
        review = db.query(A_Cinema).filter(A_Cinema.countries=='[США]').first()
    else:
        review = db.query(A_Cinema).filter(A_Cinema.countries == '[ХХХ]').first()
    if review == None :
        print ( 'Запись не найдена')
    end = time.time()
    return (f"{(end - start):.3f} сек.")

def al_group_by(db: Session):
    start = time.time()
    review = db.query(A_Cinema.movie_year, func.count(A_Cinema.movie_year)).group_by(A_Cinema.movie_year).all()
    end = time.time()
    return (f"{(end - start):.3f} сек.")

def al_sort(db: Session):
    start = time.time()
    db.query(A_Cinema).order_by(A_Cinema.countries).all()
    end = time.time()
    return (f"{(end - start):.3f} сек.")

def al_filter(db: Session):
    start = time.time()
    db.query(A_Cinema).filter(A_Cinema.countries == '[США]').all()
    end = time.time()
    return (f"{(end - start):.3f} сек.")

def al_join(db: Session):
    start = time.time()
    db.query(A_Cinema).filter(A_Cinema.id == A_Review.id).all()
    end = time.time()
    return (f"{(end - start):.3f} сек.")

def al_add_record(db: Session):
    start = time.time()
    al_record = A_Review (
        review = "ccccccccccccccccccccccccccccccccccccccccccccccccc",
        name = "что-то такое",

    )
    db.add(al_record)
    db.commit()
    end = time.time()
    return (f"{(end - start):.3f} сек.")

def al_update_records(db: Session):
    start = time.time()
    db.query(A_Cinema).filter(A_Cinema.countries ==  'test Updated').update({'countries': 'TEST'}, synchronize_session='fetch')
    db.commit()
    #query_for_filter.save()
    end = time.time()
    return (f"{(end - start):.3f} сек.")