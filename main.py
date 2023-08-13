from utils import create_database, get_info_from_employers, save_data_to_db, print_simple_table
from config import config
from db_manager import DBManager


def main():
	emp_list = {
		80: 'АльфаБанк',
		15478: 'ВК',
		78638: 'Тинькофф',
		4496: 'МТСБанк',
		3529: 'СБЕР',
		1740: 'Яндекс',
		2180: 'Озон',
		67611: 'Тензор',
		6093775: 'Астон',
		160748: 'ГНИВЦ',
		733: 'ЛАНИТ'
	}
	params = config()
	database_name = 'hh_db'

	menu_options = {
		'1': 'Получить список всех компаний и количество вакансий у каждой компании',
		'2': 'Получить список всех вакансий с расширенной информацией о вакансии',
		'3': 'Вывести среднюю зарплату по вакансиям',
		'4': 'Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям',
		'5': 'Получить список всех вакансий по ключевому слову',
		'0': 'Выход'
	}
	print(f'Запуск программы получения информации для компаний: {" ,".join(emp_list.values())}')
	# Создание БД и запись в нее полученной информации
	create_database(database_name, params)
	data = get_info_from_employers(emp_list)
	save_data_to_db(database_name, data, params)

	# Определение экземпляра класса DBManager для работы с данными БД
	db_manager = DBManager(database_name, params)
	# Запуск цикла-меню для взаимодействия с пользователем
	while True:
		print(f'Выберите опцию для взаимодействия с БД {database_name}:')
		for i, v in menu_options.items():
			print(f'{i}: {v}')
		user_option = input()
		if user_option in menu_options.keys():
			if user_option == '1':
				data = db_manager.get_companies_and_vacancies_count()
				print_simple_table([data[0], *data[1]])
			elif user_option == '2':
				data = db_manager.get_all_vacancies()
				print_simple_table([data[0], *data[1]])
			elif user_option == '3':
				data = db_manager.get_avg_salary()
				print_simple_table([data[0], *data[1]])
			elif user_option == '4':
				data = db_manager.get_vacancies_with_higher_salary()
				print_simple_table([data[0], *data[1]])
			elif user_option == '5':
				user_keyword = input('Введите ключевое слово для поиска:\n')
				data = db_manager.get_vacancies_with_keyword(user_keyword)
				print_simple_table([data[0], *data[1]])
			else:
				break
		else:
			continue


if __name__ == '__main__':
	main()
