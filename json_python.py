import json
from textwrap import indent

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)  # Преобразуем JSON-строку в Python-объект (dict)

print(parsed_data["name"])  # Выведет: Иван

data = {
    "name": "Мария",
    "age": 25,
    "is_student": True
}

json_string = json.dumps(data, indent=4)  # Преобразуем Python-объект в JSON-строку
print(json_string)


with open("json_example.json", "r", encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data)


with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)