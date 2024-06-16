import psycopg2


class DBManager:

    def __init__(self, dbname, params):
        self.dbname = dbname
        self.conn = psycopg2.connect(dbname=dbname, **params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        query = """
        SELECT company_name, 
        COUNT(*) FROM vacancies
        GROUP BY company_name
        """
        self.cur.execute(query)
        return {row[0]: row[1] for row in self.cur.fetchall()}

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на
        вакансию."""
        query = """
        SELECT job_title, company_name, salary_from, link_to_vacancy FROM vacancies
        """
        self.cur.execute(query)
        return self.cur.fetchall()

