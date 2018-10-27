import sketch


def set_max_length(difficulty_level: str) -> int:
    """
    Return an integer representing the max character length
    depending on the difficulty level given.

    :param difficulty_level:
        A string representing the level of difficulty. The
        levels are Easy, Medium, and Hard. This string can be
        upper or lower case and will work with a single character
        such as E, M and H, or the whole word, Easy, Medium and
        Hard.
    :return:
        An integer representing the max character length based on
        the difficulty level given.
    """
    difficulty_level = difficulty_level[0].upper()

    if difficulty_level == 'M':
        max_length = 6
    elif difficulty_level == 'H':
        max_length = 10
    else:
        max_length = 4
    return max_length


def display_board(
        missed_letters: str,
        correct_letters: str,
        secret_word: str
):
    """
    Shows the current state of the board, including how much of
    the secret word the player has guessed so far and the wrong
    letters the player has guessed.

    :param missed_letters:
        A string containing letters the player guessed that is
        not in secret_word.
    :param correct_letters:
        A string containing letters the player guessed that is
        in secret_word.
    :param secret_word:
        A string representing the secret word for player to guess.
    """
    print(sketch.HANGMAN_PICS[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    # replace blanks with correctly guessed letters
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    # show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=' ')
    print()


def get_guess(already_guessed: str) -> str:
    """
    Returns the letter the player entered. This function makes sure
    the player entered a single letter and not something else.

    :param already_guessed:
        A string of letters the player already guessed.
    :return:
        A string of letters the player guessed.
    """

    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def play_again() -> bool:
    """
    This function returns True if the player wants to play again;
    otherwise, it returns False.
    """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
