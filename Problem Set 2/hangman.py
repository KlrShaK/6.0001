# Problem Set 2, hangman.py
# Name: Shaurya K. Panwar
# Collaborators: None
# Time spent: 7 hours

# Hangman Game
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


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for count1 in range(len(secret_word)):
        found = False
        for count2 in range(len(letters_guessed)):
            if secret_word[count1] == letters_guessed[count2]:
                found = True
        if not found:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ''
    for count1 in range(len(secret_word)):
        found = False
        for count2 in range(len(letters_guessed)):
            if secret_word[count1] == letters_guessed[count2]:
                found = True
                guessed_word += (secret_word[count1] + ' ')
        if not found:
            guessed_word += "_ "
    return guessed_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available = ''
    for count1 in range(len(string.ascii_lowercase)):
        flag = False
        for count2 in range(len(letters_guessed)):
            if string.ascii_lowercase[count1] == letters_guessed[count2]:
                flag = True
        if not flag:
            available += string.ascii_lowercase[count1]
    return available


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    letters_guessed = ''
    print("Welcome to the game Hangman!")
    print("I'm Thinking of a Word that is", len(secret_word), "letter long")
    print("------------------------------")
    guesses_remaining = 6
    warnings_remaining = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    while not is_word_guessed(secret_word, letters_guessed):
        print("------------------------------")
        print("You have", guesses_remaining, "Guesses left.")
        available = get_available_letters(letters_guessed)
        print("Available Letters :", available)
        temp = input("Please Guess a Letter : ")
        temp = temp.lower()
        if not (temp.isalpha() and len(temp) == 1):
            warnings_remaining -= 1
            print("Oops! That is not a valid letter.", "You have", warnings_remaining, "Warnings Left :",
                  get_guessed_word(secret_word, letters_guessed))
            if guesses_remaining <= 0 or warnings_remaining <= 0:
                lost_game(guesses_remaining, warnings_remaining)
            continue
        if temp in letters_guessed:
            warnings_remaining -= 1
            print("Oops! That is not a valid letter.", "You have", warnings_remaining, "Warnings Left :",
                  get_guessed_word(secret_word, letters_guessed))
            if guesses_remaining <= 0 or warnings_remaining <= 0:
                lost_game(guesses_remaining, warnings_remaining)
            continue
        temp = temp.lower()
        letters_guessed += temp
        if temp in secret_word:
            print("Good Guess : ", get_guessed_word(secret_word, letters_guessed))
        elif temp in vowels:
            print("Oops!! That letter is not in my word :", get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 2
        else:
            print("Oops!! That letter is not in my word :", get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

        if guesses_remaining <= 0 or warnings_remaining <= 0:
            lost_game(guesses_remaining, warnings_remaining)
        if is_word_guessed(secret_word, letters_guessed):
            break
    won_game(secret_word, guesses_remaining)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def won_game(word, guesses):
    print("--------------")
    print("CONGRATULATIONS!!!, YOU WON")
    distinct = 0
    temp = ''
    for count in range(len(word)):
        if not word[count] in temp:
            distinct += 1
            temp += word[count]

    total_score = guesses * len(temp)
    print("Your Total Score for this Games is :", total_score)
    exit()


def lost_game(guesses, warnings):
    print("------------------")
    print("With Deep Grief, We would like to inform you that you just !!LOST THE GAME!! :( ")
    if guesses <= 0:
        print("YOU EXHAUSTED ALL YOUR GUESSES!!!")
    elif warnings <= 0:
        print("YOU EXHAUSTED ALL YOUR WARNINGS!!!")
    print("Psst! The Secret Word was -", secret_word)
    exit()


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    flag = False
    if len(my_word) == len(other_word):
        for count in range(len(my_word)):
            if my_word[count] == '_':
                continue
            elif my_word[count] == other_word[count]:
                flag = True
            else:
                flag = False
                break
    return flag


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    found = False
    flag = False
    for count1 in range(len(wordlist)):
        other_word = wordlist[count1]
        if len(other_word) == len(my_word):
            for count2 in range(len(my_word)):
                if my_word[count2] == '_':
                    continue
                elif my_word[count2] == other_word[count2]:
                    flag = True
                else:
                    flag = False
                    break
        if flag:
            found = True
            print(other_word, end=', ')

    if not found:
        print("\nNo Matches Found!!!")


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = ''
    print("Welcome to the game Hangman!")
    print("I'm Thinking of a Word that is", len(secret_word), "letter long")
    print("------------------------------")
    guesses_remaining = 6
    warnings_remaining = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    while not is_word_guessed(secret_word, letters_guessed):
        print("\n------------------------------")
        print("You have", guesses_remaining, "Guesses left.")
        available = get_available_letters(letters_guessed)
        print("Available Letters :", available)
        temp = input("Please Guess a Letter : ")
        temp = temp.lower()

        if temp == '*':
            print("Possible Word Matches are : ")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))

        if not (temp.isalpha() and len(temp) == 1):
            if temp != '*':
                warnings_remaining -= 1
                print("Oops! That is not a valid letter.", "You have", warnings_remaining, "Warnings Left :",
                      get_guessed_word(secret_word, letters_guessed))
                if guesses_remaining <= 0 or warnings_remaining <= 0:
                    lost_game(guesses_remaining, warnings_remaining)
                continue

        if temp in letters_guessed and temp != '*':
            warnings_remaining -= 1
            print("Oops! That is not a valid letter.", "You have", warnings_remaining, "Warnings Left :",
                  get_guessed_word(secret_word, letters_guessed))
            if guesses_remaining <= 0 or warnings_remaining <= 0:
                lost_game(guesses_remaining, warnings_remaining)
            continue
        temp = temp.lower()
        letters_guessed += temp

        if temp in secret_word:
            print("Good Guess : ", get_guessed_word(secret_word, letters_guessed))

        elif temp in vowels:
            print("Oops!! That letter is not in my word :", get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 2

        else:
            if temp != '*':
                print("Oops!! That letter is not in my word :", get_guessed_word(secret_word, letters_guessed))
                guesses_remaining -= 1

        if guesses_remaining <= 0 or warnings_remaining <= 0:
            lost_game(guesses_remaining, warnings_remaining)

        if is_word_guessed(secret_word, letters_guessed):
            break
    won_game(secret_word, guesses_remaining)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
