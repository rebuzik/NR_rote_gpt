import json
import pandas as pd
# Указываем путь к JSON-файлу
file_path = '../data/data.json'

# Открываем файл на чтение
with open(file_path, 'r', encoding='utf-8') as file:
    # Считываем содержимое файла
    json_data = file.read()

df = json.loads(json.dumps(json_data))[:5000:]

df_from_vk = pd.read_excel('../data/NR_vk_id.xlsx')
print(df)