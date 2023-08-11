from config import config
import psycopg2


class DBManager():
	"""Класс для работы с базой данных вакансий"""


	def __init__(self, db_name: str):
		"""Set the database name"""
		# self.db_name = db_name
		# self.conn = psycopg2.connect(dbname='postgres', **self.params)
		# self.conn.autocommit = True
		# self.cur = self.conn.cursor()
		# try:
		# 	with self.cur:
		# 		self.cur.execute(f'DROP DATABASE IF EXISTS {self.db_name}')
		# 		self.cur.execute(f'CREATE DATABASE {self.db_name}')
		# 		self.cur.execute(f"""CREATE TABLE employers
		# 		(
		# 		emp_id int PRIMARY KEY,
		# 		emp_name varchar(100) NOT NULL,
		# 		emp_url varchar NOT NULL
		# 		);""")
		# 		self.cur.execute(f"""CREATE TABLE vacancies
		# 		(
		# 		vac_id int PRIMARY KEY,
		# 		vac_name varchar(100) NOT NULL,
		# 		city varchar(30),
		# 		salary int NOT NULL,
		# 		vac_url varchar NOT NULL,
		# 		published_date date,
		# 		emp_id int
		# 		);
		#
		# 		ALTER TABLE vacancies ADD CONSTRAINT fk_vacancies_employers
		# 		FOREIGN KEY (emp_id) REFERENCES employers(emp_id);
		# 		""")
		# finally:
		# 	self.conn.close()



	# def __enter__(self):
	# 	pass
	#
	# def __exit__(self):
	# 	pass

	def save_data_to_database(self, employers_data: dict, vacancies_data: dict):
		pass

	def get_companies_and_vacancies_count(self):
		"""Получает список всех компаний и количество вакансий у каждой компании"""
		pass

	def get_all_vacancies(self):
		"""
		Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
		"""
		pass

	def get_avg_salary(self):
		"""Получает среднюю зарплату по вакансиям."""
		pass

	def get_vacancies_with_higher_salary(self):
		"""Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
		pass

	def get_vacancies_with_keyword(self, keyword: str):
		"""Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
		pass
