from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import CreateExercisesRequestDict, get_exercise_client
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.faker import get_random_email

# 1 создаем пользователя
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)

# 2 инициализируем два клиента  file_client и course_client
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

files_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)
exercises_client = get_exercise_client(authentication_user)

# 3 создаем файл (загружаем файл)
create_file_request = CreateFileRequestDict(
    filename='test.png',
    directory='courses',
    upload_file='./testdata/files/test.png'
)

create_file_response = files_client.create_file(create_file_request)
print('Create file data: ', create_file_response)

# 4 создаем курс
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

create_course_response = course_client.create_course(create_course_request)
print('Create course data: ', create_course_response)


# 5 создаем упражнение
create_exercises_request = CreateExercisesRequestDict(
    title = "Python",
    courseId = create_course_response['course']['id'],
    maxScore = 100,
    minScore = 20,
    orderIndex = 55,
    description = 'qwerty',
    estimatedTime = '12.12.12'
)

create_exercises_response = exercises_client.create_exercise(create_exercises_request)
print('Create exercise data: ', create_exercises_response)