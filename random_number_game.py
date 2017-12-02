import random


class RandomNumberGame:

    def __init__(self):
        pass

    def play_random_number_guessing_game(self):
        display_message = "Enter a lower number to guess between: "
        lowest_number = self._get_input_integer_from_user(display_message)
        display_message = "Enter a upper number to guess between: "
        highest_number = self._get_input_integer_from_user(display_message)
        number_to_guess = random.randint(lowest_number, highest_number)
        self._find_the_correct_number(
            lowest_number, highest_number, number_to_guess)

    def _get_input_integer_from_user(self, display_message):
        try:
            return int(raw_input(display_message))
        except:
            print "Enter an integer, you cog!"
            return self._get_input_integer_from_user(display_message)

    def _find_the_correct_number(
            self,
            lowest_number,
            highest_number,
            number_to_guess):
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
        print (
            "It took me %d attemps to guess the number %d" %
            (attempts, number_to_guess))


if __name__ == '__main__':
    random_number_game = RandomNumberGame()
    random_number_game.play_random_number_guessing_game()
