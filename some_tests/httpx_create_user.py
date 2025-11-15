import httpx
from tools.faker import get_random_email

payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=payload)
print(f"create_user_response.status_code = {create_user_response.status_code}")
print(f"create_user_response.json = {create_user_response.json()}")
