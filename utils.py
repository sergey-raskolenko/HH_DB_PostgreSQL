import psycopg2
import requests


def create_database(db_name: str, params: dict):

	conn = psycopg2.connect(dbname='postgres', **params)
	conn.autocommit = True

	with conn.cursor() as cur:
		cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
		cur.execute(f'CREATE DATABASE {db_name}')
	conn.close()

	conn = psycopg2.connect(dbname=db_name, **params)
	conn.autocommit = True

	with conn.cursor() as cur:
		cur.execute(f"""CREATE TABLE employers
		(
		emp_id int PRIMARY KEY,
		emp_name varchar(100) NOT NULL,
		emp_url varchar NOT NULL
		);""")
		cur.execute(f"""CREATE TABLE vacancies
		(
		vac_id int PRIMARY KEY,
		vac_name varchar(100) NOT NULL,
		city varchar(30),
		salary int NOT NULL,
		vac_url varchar NOT NULL,
		published_date date,
		emp_id int
		);

		ALTER TABLE vacancies ADD CONSTRAINT fk_vacancies_employers
		FOREIGN KEY (emp_id) REFERENCES employers(emp_id);
		""")
	conn.close()


def get_employer_and_vacancies_info(employer_id):
	"""Returns"""
	params = {'text': 'python', 'per_page': 100, 'area': '113'}
	vacancy_list = []

	employer_data = requests.get(f'https://api.hh.ru/employers/{employer_id}').json()

	employer_vacancies_url = employer_data.get('vacancies_url')

	response = requests.get(employer_vacancies_url, params=params).json()
	params['page'] = 0
	print(f'Получение информации о работодателе {employer_data.get("name")} и его вакансиях..')
	while params.get('page') != response.get('pages'):
		response = requests.get(employer_vacancies_url, params=params).json()
		vacancy_list.extend(response.get('items'))
		params['page'] += 1
	return {'employer': employer_data, 'vacancy_list': vacancy_list}


def get_info_from_employers(employer_ids: list):
	"""Get information"""
	return [get_employer_and_vacancies_info(employer_id) for employer_id in employer_ids]


def save_data_to_db(db_name: str, data_to_write: list, params: dict):
	conn = psycopg2.connect(dbname=db_name, **params)
	conn.autocommit = True
	print(f'Запись данных в базу данных {db_name}')
	for emp_data in data_to_write:
		emp_id = emp_data.get('employer').get('id')
		emp_name = emp_data.get('employer').get('name')
		emp_url = emp_data.get('employer').get('alternate_url')
		with conn.cursor() as cur:
			cur.execute(
				"""
				INSERT INTO employers (emp_id, emp_name, emp_url)
				VALUES (%s, %s, %s) 
				""",
				(emp_id, emp_name, emp_url)
			)
		for vacancy in emp_data.get('vacancy_list'):
			vac_id = vacancy.get('id')
			vac_name = vacancy.get('name')
			city = vacancy.get('area', {}).get('name')
			if vacancy.get('salary', {}):
				salary = vacancy.get('salary', 0).get('from', 0)
			else:
				salary = 0
			vac_url = vacancy.get('alternate_url')
			published_date = vacancy.get('published_at').split('T')[0]
			emp_id = vacancy.get('employer').get('id')
			with conn.cursor() as cur:
				cur.execute(
					"""
					INSERT INTO vacancies (vac_id, vac_name, city, salary, vac_url, published_date, emp_id)
					VALUES (%s, %s, %s, %s, %s, %s, %s) 
					""",
					(vac_id, vac_name, city, salary, vac_url, published_date, emp_id)
				)
