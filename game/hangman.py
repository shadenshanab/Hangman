import random
from words import options


HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

# options must be 5 letters or over
# options = [
#     'PROGRAMMING', 'SOFTWARE', 'JAVASCRIPT', 'PYTHON', 'DJANGO',
#     'RUBYONRAILS'
# ]

class Hangman():
    def __init__(self, word_to_guess): #constructor with base case
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_' * len(self.word_to_guess))

    def about_game(self):

        print ("""
               **************************************************************************************
               **        A Hangman Game is about guessing letters (A-Z) to form the words.         **
               **            If you guesses the right letter that is within the word,              **
               **                 the letter appears at its correct position.                      **
               **  you have to guess the correct word until a man is hung, then the game is over.  **
               ** _________________________________________________________________________________**
               **                            Get ready to play Hangman!                            **
               **************************************************************************************
               """)

    def find_indexes(self, letter): #takes a letter and returns a list with the indexes in the word to guess
        
        """for i, char in enumerate(self.word_to_guess):
             return letter == char

        for i, word_to_guess.c in self.word_to_guess:
            return letter == char"""
        
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]

    def is_invalid_letter(self, input_): # if the input is a number or a text with more than 1 char (invalid)
      
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    def print_game_status(self):  # print the word to guess blankspaces with the remaining attempts and the guessed letters

        # We append withespaces both sides to make the game look prettier
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))

    def update_progress(self, letter, indexes): # update the game progress

        for i in indexes:
            self.game_progress[i] = letter

    def get_user_input(self):
        user_input = input('\nPlease type a letter *in uppercase*: ')
        return user_input

    def play(self): #prompts the user for a letter and plays the game until the user guesses the word or lose his attempts

        self.about_game()
       
        while self.failed_attempts < len(HANGMAN): #still have chances
            self.print_game_status() #what the user have done so far
            user_input = self.get_user_input() #take letter

            # Validate the user input
            if self.is_invalid_letter(user_input):
                print('The input is not a letter!')
                continue
            # Check if the letter is not already guessed
            if user_input in self.game_progress:
                print('You already have guessed that letter')
                continue

            if user_input in self.word_to_guess: #user guessed a letter correctly
                indexes = self.find_indexes(user_input) # add the letter to its index
                self.update_progress(user_input, indexes) # update progress
                # If there is no letter to find in the word
                if self.game_progress.count('_') == 0: #count the spaces left in the word to guess
                    print('\nGood job! You won!')
                    print('The word is: {0}'.format(self.word_to_guess))
                    quit()
            else:
                self.failed_attempts += 1
        print("\nYou lost!" + 'The word is: {0}'.format(self.word_to_guess)) #if we have to chances left it leaves the loop and comes to this

if __name__ == '__main__':
    # print (options)
    word_to_guess = random.choice(options) # the options word inside (words.py) file
    hangman = Hangman(word_to_guess)
    hangman.play()