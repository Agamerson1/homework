from typing import List


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def hash_password(self, password):
        password = hash(password)

    def __str__(self):
        return f'Пользователь: {self.nickname}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.nickname == other.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Видео, название: {self.title}, длительность: {self.duration}, возрастное ограничение: {self.adult_mode}'

    def __repr__(self):
        return self.__str__()


class UrTube:
    def __init__(self):
        self.users: List[User] = list()
        self.videos: List[Video] = list()
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
            else:
                new_user = User(nickname, password, age)
                self.users.append(new_user)
                self.current_user = new_user
                print(f'Пользователь {nickname} успешно зарегистрирован и вошёл в систему')

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == self.hash_password(password):
                self.current_user = user
                print(f'Вы успешно вошли в систему, {user.nickname}')
                return
            else:
                print('Пользователь не найден или неверный пароль')

        if self.current_user is not None:
            print(f'Вы уже вошли как пользователь {self.current_user.nickname}')
            return

    def log_out(self):
        if self.current_user is None:
            print('Вход в аккаунт не выполнен')
        else:
            print(f'Вы вышли из аккаунта {self.current_user.nickname}')
            self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            title = video.title
            contains = False
            for v in self.videos:
                if title == v.title:
                    contains = True
                    break
            if contains is False:
                self.videos.append(video)

    def get_videos(self, word):
        videos_titles = []
        lower_word = word.lower()
        for video in self.videos:
            title = video.title
            lower_title = title.lower()
            if lower_word in lower_title:
                videos_titles.append(title)
        return videos_titles

    def watch_video(self, title):

        for video in self.videos:
            video_title = video.title
            if video_title == title:
                timee_now = video.time_now
                while timee_now < video.duration:
                    timee_now += 1
                    print(timee_now)
                    # sleep(1.0)
                video.time_now = 0
                print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')
