matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches) # la lista original
print(len(matches)) # tres elementos

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

print(new_list) # muesta la lista solo con lo que se quería filtrar
print(len(new_list)) # dos elementos

print(matches) #aca mantiene la lista original
print(len(matches)) # tres elementos