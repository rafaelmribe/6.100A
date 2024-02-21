# Problem Set 2, wordle.py
# Name:Rafael Moreno Ribeiro
# Collaborators:Sukrith
# Time spent:7 hours

# Wordle Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def check_user_input(secret_word, user_guess):
    """

    :param secret_word: a string, the word to be guessed
    :param user_guess: a string, the users guess
    :return: False if user_guess does not satisfy at least
	     one of the below conditions, True otherwise.
    1. must consist of only letters (uppercase or lowercase)
    2. must be the same length as secret_word
    3. must be a word found in words.txt
    """
    if len(user_guess) != len(secret_word):
        print('Oops! That word length is not correct.')
        return False
    if not user_guess.isalpha():
        print('Oops! That is not a valid word.')
        return False
    if user_guess.lower() not in wordlist:
        print('Oops! That is not a real word.')
        return False
    else:
        return True

def get_guessed_feedback(secret_word, user_guess):
    """
    :param secret_word: a string, the word to be guessed
    :param user_guess: a string, a valid user guess
    :return: a string with uppercase and lowercase letters and
	     underscores, each separated by a space (e.g. 'B _ _ S u')
    """
    s=''
    for i in range(len(user_guess)):
        if user_guess[i].lower() == secret_word[i]:
            s = s + user_guess[i].upper()
            i +=1
        elif user_guess[i].lower() in secret_word:
            s = s + user_guess[i].lower()
            i +=1
        else:
            s += '_'
            i +=1
        if i != len(user_guess):
            s += ' '
    return s

    pass

def get_alphabet_hint(secret_word, all_guesses):
    """
    takes in the secret word and a list of all previous guesses and returns a string of hint text
    :param secret_word: a string, the word to be guessed
    :param all_guesses: a list of all the previous valid guesses the user inputed
    :return: a string which replaces letters that were incorrect guesses with underscores and puts
	     semi-correct guesses (correct letter, incorrect place) in /x/
    """
    # we have coded this for you
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    out_list = []
    for char in alphabet:
        out_list.append(" "+char+" ")

    for guess in all_guesses:
        for i, char in enumerate(list(guess)):
            if char not in secret_word:
                out_list[alphabet.find(char)]=" _ "
            elif char != secret_word[i]:
                out_list[alphabet.find(char)] = "/"+char+"/"
            elif char == secret_word[i]:
                if secret_word.count(char) > guess.count(char):
                    out_list[alphabet.find(char)] = "/" + char + "/"
                else:
                    out_list[alphabet.find(char)] = "|" + char.upper() + "|"
    return "".join(out_list)

def wordle(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Wordle.

    * At the start of the game, let the user know how many letters the
      secret_word contains and how many guesses and warnings they start with.

    * The user should start with 6 guesses and 3 warnings

    * Before each round, you should display to the user how many guesses
      they have left.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a valid word!

    * The user should receive feedback immediately after each guess about
      whether their guess is valid, how closely it matches the secret_word,
      and the alphabet hint.

    * After each guess, you should display to the user the progression of
      their partially guessed words so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings = 3
    all_guesses = []
    print('Welcome to the game Wordle!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warnings} warnings remaining.')
    while guesses_remaining > 0:
        print(f'You have {guesses_remaining} guesses left.')
        user_guess = input('Please guess a word: ')
        if not check_user_input(secret_word, user_guess):
            if warnings > 0:
                warnings += -1
            else:
                guesses_remaining -= 1
            print(f'You have {warnings} warnings remaining.')
            print('-'*20)
        else:
            guesses_remaining += -1
            if user_guess.lower() == secret_word:
                print('Congratulations, you won!')
                print(f'You guessed the correct word in {6 - guesses_remaining} tries!')
                print(f'Your total score is {guesses_remaining*len(set(secret_word))}.')
                break
            else:
                all_guesses.append(user_guess)
                for i in range(0,len(all_guesses)):
                    print(get_guessed_feedback(secret_word, all_guesses[i]))
                print('Alphabet HINT:')
                print(get_alphabet_hint(secret_word, all_guesses))
            if guesses_remaining>0:
                print('-'*20)
    print(f'Sorry, you ran out of guesses. The word was {secret_word}.')

    pass

if __name__ == "__main__":
    #pass

    # To test, comment out the `pass` line above and uncomment:
    # - either of the `secret_word = ...` lines below, depending on how you want to set the secret_word
    # - the `wordle(secret_word)` line to run the game

    # uncomment and change the line below to a specific word for testing
    secret_word = "rink"

    # uncomment the line below for a randomly generated word
    #secret_word = choose_word(wordlist)
    wordle(secret_word)
