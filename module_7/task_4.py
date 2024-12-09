team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
score1 = 40
score2 = 42
print('Команда Волшебники данных решила задач: {}'.format(score2))
team1_time = 1552.512
team2_time = 2153.31451
print('Волшебники данных решили задачи за {} секунд.'.format(team2_time))
print(f'Команды решили {score1} и {score2} задач')
challenge_result = 'Победа команды Волшебники данных!'
print(f'Результат битвы: {challenge_result}')
tasks_total = score1 + score2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем {time_avg} секунд на задачу')
