import json
# Указываем путь к JSON-файлу
file_path = '../data/data.json'

# Открываем файл на чтение
with open(file_path, 'r', encoding='utf-8') as file:
    # Считываем содержимое файла
    json_data = file.read()

df = json.loads(json.dumps(json_data))[:5000:]
print(df)