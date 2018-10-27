import operative
import sketch
from random_word import RandomWords


print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = RandomWords().get_random_word(hasDictionaryDef="true", maxLength=5)
game_is_done = False

while True:
    operative.display_board(missed_letters, correct_letters, secret_word)

    # Let the player enter a letter.
    guess = operative.get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secret_word + '"! You have won!')
            game_is_done = True
    else:
        missed_letters = missed_letters + guess

        # Check if player has guessed too many times and lost.
        if len(missed_letters) == len(sketch.HANGMAN_PICS) - 1:
            operative.display_board(missed_letters, correct_letters, secret_word)
            print('You have run out of guesses!\nAfter '
                  + str(len(missed_letters))
                  + ' missed guesses and '
                  + str(len(correct_letters))
                  + ' correct guesses, the word was "'
                  + secret_word + '"')
            game_is_done = True

    # Ask the player if they want to play again (but only if the game is done).
    if game_is_done:
        if operative.play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = RandomWords().get_random_word(hasDictionaryDef="true", maxLength=5)
        else:
            break
