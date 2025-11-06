import httpx
from tools.faker import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data: ', create_user_response_data)

login_user_payload = {
    "email": create_user_payload["email"],
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_user_payload)
login_response_data = login_response.json()
print(f"login_response.status_code = {login_response.status_code}")
print(f"login_response_data = {login_response_data}")

USER_ID = create_user_response_data["user"]["id"]

get_user_token = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

delete_user_response = httpx.delete(
    f"http://localhost:8000/api/v1/users/{USER_ID}", headers=get_user_token)
delete_user_response_data = delete_user_response.json()
print(f"delete_user_response.status_code = {delete_user_response.status_code}")



