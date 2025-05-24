import csv
import json

def load_words_from_csv(file_path):
  with open(file_path, 'r') as f:
    reader = csv.reader(f)
    words = []
    for row in reader:
      if row:
        words.append(row[0])
    return words
  
def load_definitions_from_json(file_path):
  with open(file_path, 'r') as f:
    definitions = json.load(f)
  return definitions

def test_user(words, definitions):
  top_score = 0
  encountered_words = set()
  for word in words:
    print(f'\nDefine: {word}')


    if word not in definitions:
      print(
      'Definition not found for this word. Skipping...')

    definition = definitions[word]
    if word not in encountered_words:
      print(f'{word} -> {definition}')

    
    user_input = input('Answer: ')

    if user_input.lower() != definition.lower():
      print('\nGame Over!')
      print(f'Top Score: {top_score}')
      print(f'You failed on: {word}')
      print(f'Correct Definition: {definition}')
      return
    
    encountered_words.add(word)
    top_score += 1
    print('Correct!')

  print('\nCongratulations You have won the game')
  print(f'Top Score: {top_score}')



if __name__ == "__main__":
  csv_file_path = 'word_history.csv'
  json_file_path = 'definitions.json'

  words = load_words_from_csv(csv_file_path)
  definitions = load_definitions_from_json(json_file_path)

  print("welcome to the word game!")
  test_user(words, definitions)