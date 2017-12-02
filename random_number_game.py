import random


class RandomNumberGame:

    def __init__(self):
        self.computer_number_of_games_played = 0
        self.human_number_of_games_played = 0

    def play_computer_random_number_guessing_game(self):
        lowest_number, highest_number, number_to_guess = self._set_up_game()
        self._computer_find_the_correct_number(lowest_number, highest_number, number_to_guess)
        self.computer_number_of_games_played = self.human_number_of_games_played + 1
        
    def play_human_random_number_guessing_game(self):
        lowest_number, highest_number, number_to_guess = self._set_up_game()
        self._human_find_the_correct_number(lowest_number, highest_number, number_to_guess)
        self.human_number_of_games_played = self.human_number_of_games_played + 1
        
    def _set_up_game(self):
        display_message = "Enter a lower number to guess between: "
        lowest_number = self._get_input_integer_from_user(display_message)
        display_message = "Enter a upper number to guess between: "
        highest_number = self._get_input_integer_from_user(display_message)
        number_to_guess = random.randint(lowest_number, highest_number)
        return lowest_number, highest_number, number_to_guess

    def _get_input_integer_from_user(self, display_message):
        try:
            return int(raw_input(display_message))
        except:
            print "Enter an integer, you cog!"
            return self._get_input_integer_from_user(display_message)

    def _computer_find_the_correct_number(self, lowest_number, highest_number, number_to_guess):
        computer_guess = lowest_number
        attempts = 0
        highest = highest_number
        lowest = lowest_number
        while(computer_guess != number_to_guess):
            print computer_guess
            attempts = attempts + 1
            if computer_guess < number_to_guess:
                lowest = computer_guess
                computer_guess = random.randint(lowest, highest) + 1
            if computer_guess > number_to_guess:
                highest = computer_guess
                computer_guess = random.randint(lowest, highest) - 1
        print ("It took the computer %d attempts to guess the number %d" % (attempts, number_to_guess))

    def _human_find_the_correct_number(self, lowest_number, highest_number, number_to_guess):
        display_message = "Guess a number"
        user_guess = self._get_input_integer_from_user(display_message)
        attempts = 1
        while not user_guess == number_to_guess:
            if user_guess < number_to_guess:
                print "Nope, guess higher!"
            elif user_guess > number_to_guess:
                print "Nope, guess lower!"
            user_guess = self._get_input_integer_from_user(display_message)
            attempts = attempts + 1
        print ("It only took you %d attempts to guess the number %d" % (attempts, number_to_guess))

if __name__ == '__main__':
    random_number_game = RandomNumberGame()
    display_message = "Do you want to play another game? 1 for yes and anything else will be a no."
    user_choice = raw_input(display_message)
    while user_choice == '1':
        human_or_computer_message = "Computer or human game? 1 for computer and anything else will be human."
        if raw_input(human_or_computer_message) == '1':
            random_number_game.play_computer_random_number_guessing_game()
        else:
            random_number_game.play_human_random_number_guessing_game()
        user_choice = raw_input(display_message)
    print ("You did %d computer and %d human games"
           % (random_number_game.computer_number_of_games_played,
              random_number_game.human_number_of_games_played))
