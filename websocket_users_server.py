import asyncio
import websockets


async def handle_client(websocket):
    """Обработчик подключения клиента"""
    # Получаем сообщение от клиента
    message = await websocket.recv()
    print(f"Получено сообщение от пользователя: {message}")

    # Отправляем пять ответных сообщений
    for i in range(1, 6):
        response = f"{i} Сообщение пользователя: {message}"
        await websocket.send(response)


async def main():
    """Запуск сервера"""
    async with websockets.serve(handle_client, "localhost", 8765):
        print("WebSocket сервер запущен на ws://localhost:8765")
        print("Ожидание подключений...")
        await asyncio.Future()  # Держим сервер запущенным


asyncio.run(main())
