list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# TODO Разделите участников на две команды
count_players = len(list_players)
average_players = count_players // 2
comand_first = list_players[:average_players]
comand_second = list_players[average_players:]
print(comand_first)
print(comand_second)
