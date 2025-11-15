from concurrent import futures
import grpc
import course_service_pb2
import course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация сервиса CourseService"""

    def GetCourse(self, request, context):
        """
        Обработчик метода GetCourse

        Args:
            request: GetCourseRequest с course_id
            context: контекст gRPC

        Returns:
            GetCourseResponse с информацией о курсе
        """
        print(f"Получен запрос для course_id: {request.course_id}")

        # Формируем ответ
        response = course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )

        return response


def serve():
    """Запуск gRPC-сервера"""
    # Создаем сервер с пулом потоков
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Регистрируем наш сервис
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(
        CourseServiceServicer(), server
    )

    # Настраиваем прослушивание порта 50051
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC-сервер запущен на порту 50051...")

    # Ждем завершения
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
