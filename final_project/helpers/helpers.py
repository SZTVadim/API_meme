import os
import allure

this_file = os.path.dirname(__file__)
file_path = os.path.join(os.path.dirname(this_file), ".env")

TEST_DATA = {'text': 'Test', 'tags': ['test_tag'], 'info': {'info': 'test_info'}, 'url': 'test_url'}


def open_file(type_opening):  # открываем файл, где должен храниться токен
    with open(file_path, type_opening) as file:
        data_file = file.readlines()
        return data_file


def check_in_dotenv(key):  # проверяем, есть ли в файле .env наш токен
    lines = open_file('r')
    for line in lines:
        if line.strip().startswith(f'{key}='):
            return line.split('=')[1].strip()
    return None


@allure.step('Добавление актуального токена в файл .env')
def add_in_dotenv(token):  # добавление токена в файл .env
    with open(file_path, "a") as file:
        file.write(f"TOKEN={token}\n")


def delete_last_from_dotenv(key):  # удаление тестового токена из файла .env
    lines = open_file('r')
    last_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith(f'{key}='):
            last_index = i

    # Если такой ключ не найден — ничего не делаем
    if last_index is None:
        return

    # Записываем все строки, кроме той, которую хотим удалить
    with open(file_path, 'w') as write_file:
        for i, line in enumerate(lines):
            if i != last_index:
                write_file.write(line)
