# data_processing.py
import json
import pandas as pd
from datasets import load_dataset
from collections import defaultdict


def process_data(file_path, number):
    # Загружаем набор данных из JSON-файла
    dataset = load_dataset('json', data_files=file_path)

    # Извлекаем данные для указанного номера
    person_data = dataset['train'][number]

    name = f"{person_data['surname']} {person_data['name']} {person_data['patronymic']}"
    birthday = person_data['birthday']
    search_engines = ', '.join(person_data['search engines'][0][:5000]) if person_data['search engines'] else ''
    eyes_of_god = person_data['eog']

    # Извлекаем данные VK, фильтруя нулевые значения и пустые списки
    vk_data = []
    if person_data['vk'] is not None:
        vk_data = [item for item in person_data['vk'] if item is not None and item != []]

    # Создаем словарь для подсчета количества групп по тематикам
    group_count = defaultdict(int)
    vk_group = ''

    # Обработка данных VK
    for group in vk_data:
        name, theme_list = group[0], group[1]

        # Предполагаем, что первый элемент списка тематик содержит строку с названием и тематикой, разделенными ":"
        if theme_list:
            theme_str = theme_list
            # Разделяем строку по ":"
            theme_parts = theme_str.split(':')
            if len(theme_parts) == 2:  # Убеждаемся, что разделение прошло успешно
                # Извлекаем только тематику
                theme = theme_parts[1].strip()
                # Увеличиваем счетчик для данной тематики
                group_count[theme] += 1

    # Формирование строки с информацией о группах VK
    for theme, count in group_count.items():
        vk_group += f"{theme}, {count}\n"

    return name, birthday, search_engines, eyes_of_god, vk_group

# Пример вызова функции
if __name__ == "__main__":
    file_path = '../data/data.json'
    number = 3
    name, birthday, search_engines, eyes_of_god, vk_group = process_data(file_path, number)
    print("Name:", name)
    print("Birthday:", birthday)
    print("Search Engines:", search_engines)
    print("Eyes of God:", eyes_of_god)
    print("VK Groups:", vk_group)
