import httpx

"""
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#print(response)
#print(response.status_code)
#print(response.text)

data_req = {
    "userId": 1,
    "title": "Hello World !!!!",
    "completed": False
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data_req)

#print(response.json())
#print(response.text)


data_params = {
    "userId": 1,
    "title": "Hello World !!!!"
}
response = httpx.post("https://httpbin.org/post", data=data_params)
#print(response.json())
#print(response.text)
#print(response.request.headers)


headers  = {
    "Content-Type": "application/json",
    "Auth" : "Beer my_token"
}
response = httpx.get("https://httpbin.org/get", headers=headers)

#print(response.json())

params = {
    "userId": 1
}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

#print(response.url)
#print(response.json())


# ------- send FILE -----

files = {
    "file": open("example.txt", "rb")
}


files = {"file": ("example.txt", open("example.txt", "rb"))}

response = httpx.post("https://httpbin.org/post", files=files)
print(response.headers)
print(response.text)



# Работа с сесиями в контекстном менеджере

with httpx.Client() as client:
    response1 = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = httpx.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())
print(response2.json())



# тут заголовки клиент сам будет автоматом прокидывать в запрос
client = httpx.Client(headers={"Authorization": "Bearer my_token_secret"})
response = client.get("https://httpbin.org/get")
print(response.text)

"""

# работа с ошибками

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/todos/error")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Error - {e}")


# запрос с задержкой

try:
    response = httpx.get("https://postman-echo.com/delay/5", timeout=2)
except httpx.ReadTimeout as e:
    print(f"Запрос привысил лимит времени (2) {e}")