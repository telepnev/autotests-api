import grpc
import course_service_pb2
import course_service_pb2_grpc


def run():
    """Запуск gRPC-клиента"""
    # Устанавливаем соединение с сервером
    with grpc.insecure_channel('localhost:50051') as channel:
        # Создаем stub (заглушку) для вызова методов сервиса
        stub = course_service_pb2_grpc.CourseServiceStub(channel)

        # Формируем запрос
        request = course_service_pb2.GetCourseRequest(course_id="api-course")

        # Вызываем метод GetCourse
        print("Отправка запроса на сервер...")
        response = stub.GetCourse(request)

        # Выводим ответ
        print("\nПолученный ответ:")
        print(response)


if __name__ == '__main__':
    run()
