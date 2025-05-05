import os
import allure

this_file = os.path.dirname(__file__)
file_path = os.path.join(os.path.dirname(this_file), ".env")


def open_file(type_opening):
    with open(file_path, type_opening) as file:
        data_file = file.readlines()
        return data_file


def check_in_dotenv(key):
    lines = open_file('r')
    for line in lines:
        if line.strip().startswith(f'{key}='):
            return line.split('=')[1].strip()
        return None


@allure.step('Добавление актуального токена в файл .env')
def add_in_dotenv(token):
    with open(file_path, "a") as file:
        file.write(f"TOKEN={token}\n")


@allure.step('удаление протухшего токена из файла .env')
def delete_from_dotenv(key):
    lines = open_file('r')
    with open(file_path, 'w') as write_file:
        write_file.writelines(line for line in lines if not line.strip().startswith(f'{key}='))
