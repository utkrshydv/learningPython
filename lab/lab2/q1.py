import random
number_to_guess = random.randint(1, 10)

while True:
  guess = int(input("Guess a number between 1 and 10: "))

  if guess < number_to_guess:
    print("guess higher")
    continue
  elif guess > number_to_guess:
    print("guess lower")
    continue
  else: 
    print("Correct!")
    break
