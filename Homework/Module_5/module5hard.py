# "Свой YouTube"
from time import sleep


class User:

    def __init__(self, nickname: str, password: hash, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users and self.users[nickname].password == hash(password):
            self.current_user = nickname
            print(f"Пользователь {nickname} вошёл в систему.")
        else:
            print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users[nickname] = User(nickname, hash(password), age)
            self.current_user = nickname
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None
        print('Произведён выход из системы')

    def add(self, *args):
        for item in args:
            if item not in self.videos:
                self.videos[item.title] = Video(item.title, item.duration, item.time_now, item.adult_mode)
            else:
                pass

    def get_videos(self, word):
        keys = list(self.videos.keys())
        result = []
        for item in keys:
            if word.lower() in item.lower():
                result.append(item)
        return result

    def watch_video(self, title):
        if title in self.videos:
            if self.current_user is not None:
                if self.users[self.current_user].age >= 18:
                    for i in range(self.videos[title].duration):
                        self.videos[title].time_now += 1
                        print(self.videos[title].time_now, end=' ')
                        sleep(1)
                        if self.videos[title].time_now == self.videos[title].duration:
                            print('Конец видео')
                            self.videos[title].time_now = 0
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
