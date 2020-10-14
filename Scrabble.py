letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters += [
  letter.lower()
  for letter
  in letters
]

points += [
  num
  for num
  in points
]


letter_to_points = {key:value for key, value in zip(letters, points)}

letter_to_points[' '] = 0


name = [input('Can you tell me the player\'s name please? ')]

if input('Are there any other players whose scores you would like to check? (y/n) ') == 'y':
  name.append(input('Please enter the other player\'s name: '))
else:
  pass

words = []

for i in name:
  words.append([input('Can you give me ' + i + '\'s words to score seperated by commas please? ')])


def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

player_to_words = {key:value for key, value in zip(name, words)}

for name in player_to_words:
  print(name + ' has played the following words: ')
  print(player_to_words[name])

player_to_points = {}

def update_points_total():  
  for player, words in player_to_words.items():
    for word in words:
      player_points = 0
      player_points += score_word(word)
      player_to_points[player] = player_points
      print (player + ' has ' + str(player_to_points[player]) + ' points')
  return player_to_points

update_points_total()
    
# while input('Would you like to add any more words? ') == 'y':
#   for player in player_to_words: 
#     player_to_words[player].append(input('Can you give me ' + player + '\'s words to score seperated by commas please? '))
#   print(player_to_words)
#   update_points_total()