## Описание
Программа, которая получает информацию об необходимых компаниях и их вакансиях с платформы HeadHunter в России
**hh.ru** ([ссылка на API](https://github.com/hhru/api/blob/master/docs/general.md))

## Особенности реализации
1. Создан парсер конфигураций для подключения к базе данных (БД).
2. Реализованы функциональности для создания БД с необходимой структурой и записи в нее данных, 
получении информации с сервиса, вывода данных в табличном виде в консоль.
3. БД содержит следующие таблицы:
- `employers`, c полями: emp_id - ID компании, emp_name - название компании, emp_url: ссылка на компанию) 
- `vacancies`, с полями: vac_id - ID вакансии, vac_name- название вакансии, city - город работы, salary - зарплата, 
vac_url - ссылка на вакансию , published_date - дата публикации, emp_id - ID компании)
4. Для работы с БД создан класс `DBManager`, с методами для получения определенной информации:
- `get_companies_and_vacancies_count()`: получает список всех компаний и количество вакансий у каждой компании.
- `get_all_vacancies()`: получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и
ссылки на вакансию.
- `get_avg_salary()`: получает среднюю зарплату по вакансиям.
- `get_vacancies_with_higher_salary()`: получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
- `get_vacancies_with_keyword()`: получает список всех вакансий, в названии которых содержатся переданные в метод слова, 
например “python”.
5. Реализовано функциональное меню для взаимодействия с пользователем.


## Как запустить проект
1. Клонируйте проект с github:
[github.com/sergey-raskolenko/HH_DB_PostgreSQL](https://github.com/sergey-raskolenko/HH_DB_PostgreSQL)
2. Создайте конфигурационный файл `database.ini` с вашими данными для подключения к PostgreSQL следующего содержания:
 ```
[postgresql]
host=localhost
user=your_user
password=your_password
port=5432
```
3. Создайте poetry venv и установите зависимости при помощи терминала:
`poetry install`
4. Отредактируйте словарь `emp_list` в файле `main.py` согласно вашим требованиям по компаниям.
5. Запустите файл `main.py` по адресу /HH_DB_PostgreSQL

## Ход работы

После запуска программы создается БД, происходит сбор информации по компаниям и вакансиям и ее запись в БД.

Осуществляется вход в функциональное меню со следующими вариантами, исходя из ввода пользователя:
* 1 - Получить список всех компаний и количество вакансий у каждой компании
* 2 - Получить список всех вакансий с расширенной информацией о вакансии
* 3 - Вывести среднюю зарплату по вакансиям
* 4 - Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям
* 5 - Получить список всех вакансий по ключевому слову
* 0 - Выход



## Выходные данные

- Информация о компаниях/вакансиях, полученная с платформы HeadHunter, сохраненная в БД PostgreSQL.
- Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.


### Используемые технологии
* python (3.11)
* requests
* psycopg2




