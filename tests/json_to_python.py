import json

"""
++++из Json строки мы приобразауюем в СЛОВАРь, те Json это словарь в Питоне
"""

# строка в нутри которой джейсон
# строка
json_data = '{"name": "Geka", "age": 43, "is_student": true}'
print(type(json_data))  # <class 'str'>
print(json_data)  # {"name": "Geka", "age": 43, "is_student": true}

# конвектировали в словарь
parsed_json_data = json.loads(json_data)
print(type(parsed_json_data))  # <class 'dict'>
print(parsed_json_data)  # {'name': 'Geka', 'age': 43, 'is_student': True}

big_json = """
{
  "email": "user@example.com",
  "lastName": "string",
  "age": 43,
  "is_student": true,
  "courses": ["QA", "Python", "Java", {"same_object": "Тут может быть какой то объект"}],
  "address": {
    "city": "Moscow",
    "zip_code": 100500
  }
}
"""

parsed_big_json_data = json.loads(big_json)
print(type(parsed_big_json_data))
print(parsed_big_json_data)

print(parsed_big_json_data['courses'])

"""

        Сохранение JSON (сериализация)
++++Приобразуем СЛОВАРЬ в JSON строку 
"""

data = {
    'email': 'user@example.com',
    'lastName': 'Евгений',
    'age': 43,
    'is_student': True,
}

json_data = json.dumps(data, indent=2)
print(json_data) # {"email": "user@example.com", "lastName": "string", "age": 43, "is_student": true}
print(type(json_data)) # <class 'str'>


"""
++++парсим json из файла и обратно
"""

# reading
with open("json_exemp.json", 'r', encoding='utf-8') as json_file:
    data_from_file = json.load(json_file)
    print(data_from_file) #на выходе приходит СЛОВАРЬ
    print(type(data_from_file)) # <class 'dict'>

# writing
with open("json_from_python.json", 'w', encoding='utf-8') as file:
    # данные data взял выше по коду
    file.write(json.dumps(data, indent=2, ensure_ascii=False))