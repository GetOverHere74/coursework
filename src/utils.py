import psycopg2
from hh_parser import get_vacancies, get_companies, get_vacancies_list

data = get_vacancies(get_companies())
vacancies = get_vacancies_list(data)


def create_db(name, params):
    """Создание базы данных и таблиц для сохранения данных о компаниях и вакансиях."""
    try:
        conn = psycopg2.connect(dbname='postgres', **params)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f'DROP DATABASE IF EXISTS {name}')
        cur.execute(f'CREATE DATABASE {name}')
        conn.close()

        conn = psycopg2.connect(dbname=name, **params)
        with conn.cursor() as cur:
            cur.execute(f'CREATE TABLE IF NOT EXISTS employers '
                        f'(company_id int, company_name varchar(100), company_url varchar (100))')
        with conn.cursor() as cur:
            cur.execute(f'CREATE TABLE IF NOT EXISTS vacancies (company_name varchar (100), job_title varchar(100), '
                        f'link_to_vacancy varchar(100), salary_from int, currency varchar(10), '
                        f'description text, requirement text)')
        conn.commit()
        conn.close()

        return "База данных и таблицы успешно созданы."

    except Exception as e:
        return f"Произошла ошибка: {e}"
