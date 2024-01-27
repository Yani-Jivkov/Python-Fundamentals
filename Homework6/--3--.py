cards = input()

team_a = set()
team_b = set()
players_a = 11
players_b = 11

for card in cards.split():
    team, player = card.split('-')
    player_num = int(player)

    if team == 'A' and player_num not in team_a:
        team_a.add(player_num)
        players_a -= 1
    elif team == 'B' and player_num not in team_b:
        team_b.add(player_num)
        players_b -= 1

    if players_a < 7 or players_b < 7:
        result = f"Team A - {players_a}; Team B - {players_b}\nGame was terminated"
        break
else:
    result = f"Team A - {players_a}; Team B - {players_b}"

print(result)
