from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict


class UpdateUserRequest(TypedDict):
    # в словаре можно
    email: str | None
    password: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):

    def get_get_user_me_api(self) -> Response:
        return self.get("/api/v1/users/me")

    def get_user_me_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequest) -> Response:
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        return self.delete(f"/api/v1/users/{user_id}")
