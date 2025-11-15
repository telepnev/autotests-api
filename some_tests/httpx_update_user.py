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
UPDATE_EMAIL_USER = get_random_email()

get_user_token = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

update_user_payload = {
    "email": UPDATE_EMAIL_USER,
    "lastName": "string999_888",
    "firstName": "string999_888",
    "middleName": "string999_888"
}

update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{USER_ID}",
    headers=get_user_token,
    json=update_user_payload
)

update_user_response_data = update_user_response.json()
print(f"update_user_response.status_code = {update_user_response.status_code}")
print(f"update_user_response_data = {update_user_response_data}")
