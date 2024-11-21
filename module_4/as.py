import hashlib
import time


# Класс User
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Хэширование пароля
        self.age = age

    def __str__(self):
        return f"User(nickname={self.nickname}, age={self.age})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.nickname == other.nickname


# Класс Video
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Video(title={self.title}, duration={self.duration}s, adult_mode={self.adult_mode})"

    def __repr__(self):
        return self.__str__()


# Класс UrTube
class UrTube:
    def __init__(self):
        self.users = []  # Список пользователей
        self.videos = []  # Список видео
        self.current_user = None  # Текущий пользователь

    def log_in(self, nickname, password):
        if self.current_user is not None:
            print(f"Вы уже вошли как {self.current_user.nickname}")
            return

        for user in self.users:
            if user.nickname == nickname and user.password == hashlib.sha256(password.encode()).hexdigest():
                self.current_user = user
                print(f"Вход выполнен успешно. Добро пожаловать, {user.nickname}!")
                return
        print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)  # После регистрации сразу выполняется вход

    def log_out(self):
        if self.current_user is None:
            print("Вы не вошли в аккаунт.")
        else:
            print(f"Выход выполнен. До свидания, {self.current_user.nickname}.")
            self.current_user = None

    def add(self, *videos):
        for video in videos:
            if all(v.title != video.title for v in self.videos):
                self.videos.append(video)
            else:
                print(f"Видео с названием {video.title} уже существует.")

    def get_videos(self, search_term):
        search_term = search_term.lower()
        result = [video.title for video in self.videos if search_term in video.title.lower()]
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print("Видео не найдено.")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Начинаем просмотр видео: {video.title}")
        while video.time_now < video.duration:
            print(video.time_now + 1, end=' ', flush=True)
            time.sleep(1)  # Имитируем просмотр по секундам
            video.time_now += 1
        print("\nКонец видео")


# Проверка работы программы
ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))  # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # Войдите в аккаунт, чтобы смотреть видео

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')  # Вам нет 18 лет, пожалуйста покиньте страницу

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')  # 1 2 3 4 5 6 7 8 9 10 Конец видео

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)  # urban_pythonist

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')  # Видео не найдено
