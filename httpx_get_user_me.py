import httpx

USER_LOGIN = "telepnef_ex@example.com"
USER_PASSWORD = "telepnef777"

login_payload = {
    "email": USER_LOGIN,
    "password": USER_PASSWORD
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f"login_response.status_code = {login_response.status_code}")
print(f"login_response.json() = {login_response.json()}")

ACCESS_TOKEN = f"Bearer {login_response_data['token']['accessToken']}"

headers = {"Authorization": ACCESS_TOKEN}

users_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(f"users_me_response.status_code = {users_me_response.status_code}")
print(f"users_me_response.json = {users_me_response.json()}")


"""
поправил название коммита
"""
