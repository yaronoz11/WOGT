def welcome():
    name = input('What is your name?')
    print(f'Hi {name} and welcome to the World of Games: The Epic Journey')


def start_play():
    while True:
        try:
            game_number = """        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
        2. Guess Game - guess a number and see if you chose like the computer.
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS.
"""
            print(game_number)

            difficulty_level = int(input('Enter a game number: '))
            if difficulty_level not in [1, 2, 3]:
                print('Out of range. Please enter a number between 1 and 3.')
                continue

            difficulty_level = int(input('Choose a difficulty level between 1-5: '))
            if difficulty_level < 1 or difficulty_level > 5:
                print('Difficulty level out of range. Please enter a number between 1 and 5.')
                continue

            return f'You chose game number {difficulty_level} and difficulty level {difficulty_level}'

        finally:
            print('Invalid input. Please enter a valid integer.')
