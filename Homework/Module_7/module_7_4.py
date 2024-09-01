# "Форматирование строк"
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total


def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды "Мастера кода"!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды "Волшебники Данных"!'
    else:
        result = 'Ничья!'
    return result


# Использование %
print('В команде "Мастера кода": %d участников.' % team1_num)
print('В команде "Волшебники данных": %d участников.' % team2_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))

# Использование format():
print('Команда "Волшебники данных" решила задач: {}!'.format(score_2))
print('"Волшебники данных" решили задачи за {} с.!'.format(round(team2_time, 1)))

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!.')

print(challenge_result())
