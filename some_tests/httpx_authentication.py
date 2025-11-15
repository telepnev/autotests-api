import httpx

login_payload = {
    "email": "telepnef_ex@example.com",
    "password": "telepnef777"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f"login_response.json = {login_response_data}")
print(f"login_response.status_code = {login_response.status_code}")


refresh_payload = {
"refreshToken": login_response_data["token"]["refreshToken"]
}

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()
print(f"refresh_response.json = {refresh_response_data}")
print(f"refresh_response.status_code = {refresh_response.status_code}")
