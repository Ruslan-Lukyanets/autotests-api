import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1", verify=False)

print(response.status_code)  # 200
print(response.json())  # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)  # 201 (Created)
print(response.json())  # Ответ с созданной записью

data = {"username": "test_user", "password": "123456"}

response = httpx.post("https://postman-echo.com/post", data=data, verify=False)

print(response.json())  # {'form': {'username': 'test_user', 'password': '123456'}, ...}

headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://postman-echo.com/get")

print(response.json())

params =  {"userId": 1}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)
print(response.json())

files = {"file" : ("example.txt", open("example.txt", "rb"))}

response = httpx.post("https://postman-echo.com/post", files=files)

print(response.json())

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())
print(response2.json())

client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://postman-echo.com/get")

print(response.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/ivalid-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

try:
    response = httpx.get("https://postman-echo.com/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил таймаут времени")