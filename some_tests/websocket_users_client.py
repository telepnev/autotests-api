import asyncio
import websockets


async def main():
    """Подключение к серверу и обмен сообщениями"""
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        # Отправляем сообщение серверу
        message = "Привет, сервер!"
        await websocket.send(message)
        print(f"Отправлено сообщение: {message}")

        # Получаем пять сообщений от сервера
        print("\nПолученные ответы от сервера:")
        for _ in range(5):
            response = await websocket.recv()
            print(response)


asyncio.run(main())
