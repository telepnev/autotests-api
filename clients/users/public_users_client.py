from httpx import Response

from clients.api_client import ApiClient
from typing import TypedDict


class CreateUserRequest(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(ApiClient):
    """
       Клиент для работы с /api/v1/users
       """
    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Метод для создания нового пользователя.

        :param request: Словарь с email,password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post("/api/v1/users", json=request)
