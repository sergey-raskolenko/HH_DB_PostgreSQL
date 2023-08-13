from typing import Tuple, List, Any
import psycopg2


class DBManager:
	"""Класс для работы с базой данных вакансий"""
	def __init__(self, db_name: str, params: dict) -> None:
		"""
		Инициализатор параметров для подключения к БД
		:param db_name: Имя БД
		:param params: Параметры для подключения к БД
		"""
		self.db_name = db_name
		self.params = params

	def get_companies_and_vacancies_count(self) -> Tuple[List[str], List[tuple[Any, ...]]]:
		"""Получает список всех компаний и количество вакансий у каждой компании"""
		conn = psycopg2.connect(dbname=self.db_name, **self.params)
		conn.autocommit = True

		with conn.cursor() as cur:
			cur.execute(
				"""
				SELECT employers.emp_name, COUNT(*) FROM vacancies
				JOIN employers ON employers.emp_id=vacancies.emp_id
				GROUP BY employers.emp_name
				"""
			)
			data = cur.fetchall()
		conn.close()
		return ['Company name', 'Numbers of vacancies'], data

	def get_all_vacancies(self) -> Tuple[List[str], List[tuple[Any, ...]]]:
		"""
		Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
		"""
		conn = psycopg2.connect(dbname=self.db_name, **self.params)
		conn.autocommit = True

		with conn.cursor() as cur:
			cur.execute(
				"""
				SELECT e.emp_name, v.vac_name, v.salary, v.vac_url FROM vacancies AS v
				JOIN employers AS e ON  e.emp_id=v.emp_id
				"""
			)
			data = cur.fetchall()
		conn.close()
		return ['Company name', 'Vacancy name', 'Salary', 'Vacancy link'], data

	def get_avg_salary(self) -> Tuple[List[str], List[tuple[Any, ...]]]:
		"""Получает среднюю зарплату по вакансиям."""
		conn = psycopg2.connect(dbname=self.db_name, **self.params)
		conn.autocommit = True

		with conn.cursor() as cur:
			cur.execute(
				"""
				SELECT AVG(salary) FROM vacancies
				WHERE salary > 0
				"""
			)
			data = cur.fetchall()[0][0]
		conn.close()
		if not data:
			data = 0
		else:
			data = float(data)
		return ['Description', 'Quantity'], [('Average salary', data)]

	def get_vacancies_with_higher_salary(self) -> Tuple[List[str], List[tuple[Any, ...]]]:
		"""Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
		conn = psycopg2.connect(dbname=self.db_name, **self.params)
		conn.autocommit = True

		with conn.cursor() as cur:
			cur.execute(
				"""
				SELECT e.emp_name, v.vac_name, v.salary, v.vac_url FROM vacancies AS v
				JOIN employers AS e ON  e.emp_id=v.emp_id
				WHERE v.salary > (SELECT AVG(salary) FROM vacancies WHERE salary > 0)
				"""
			)
			data = cur.fetchall()
		conn.close()
		return ['Company name', 'Vacancy name', 'Salary', 'Vacancy link'], data

	def get_vacancies_with_keyword(self, keyword: str) -> Tuple[List[str], List[tuple[Any, ...]]]:
		"""Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
		conn = psycopg2.connect(dbname=self.db_name, **self.params)
		conn.autocommit = True

		with conn.cursor() as cur:
			cur.execute(
				f"""
				SELECT * FROM vacancies as v
				WHERE v.vac_name LIKE '%{keyword.lower()}%' or v.vac_name LIKE '%{keyword.upper()}%' or
				v.vac_name LIKE '%{keyword.capitalize()}%'
				"""
			)
			data = cur.fetchall()
		conn.close()
		return ['VacancyID', 'Vacancy name', 'City', 'Salary', 'Vacancy link','Published date', 'EmployerID'], data
