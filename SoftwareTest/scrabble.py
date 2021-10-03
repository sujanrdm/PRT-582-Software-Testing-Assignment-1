import enchant
import time
import random

from past.builtins import raw_input


def game():
    letter_value = {}
    start = 'A'
    for AsciiValue in range(26):  # iterates all the alphabets from A to Z
        letter_value[chr(ord(start) + AsciiValue)] = 1  # The alphabets are converted to ASCII value to get number

    temp = ['D', 'G']
    for val in temp:
        letter_value[val] += 1  # The values are stored as 2 for these alphabets by adding up to initial one and so on
    temp = ['B', 'C', 'M', 'P']
    for val in temp:
        letter_value[val] += 2
    temp = ['F', 'H', 'V', 'W', 'Y']
    for val in temp:
        letter_value[val] += 3
    temp = ['K']
    for val in temp:
        letter_value[val] += 4
    temp = ['J', 'X']
    for val in temp:
        letter_value[val] += 7
    temp = ['Q', 'Z']
    for val in temp:
        letter_value[val] += 9

    check_word = enchant.Dict("en_US")  # verifies if the word is a valid english word
    final_score = 0
    print("--Go Gamer! Your 15 seconds timer starts now--")
    while True:
        start_time = time.time()
        length = random.randint(2, 7)  # random word length is generated
        question = 'Enter english word of length {} chars: '.format(length)
        phrase = input(question)
        question.format(length)
        end_time = time.time()
        final_time = end_time - start_time

        # validates the condition for time, word and length
        if final_time > 15 or not check_word.check(phrase) or len(phrase) != length:
            if final_time > 15:
                print("Sorry! You ran out of time. Please enter $1 coin to Replay")
                break
            elif not check_word.check(phrase):
                print("Sorry! The this is not a  valid word")
            elif len(phrase) != length:
                print("The length is not invalid length, Please retype")

        else:
            for val in phrase:
                final_score += letter_value[val.upper()]  # the score is calculated and reflected
            break

    final_time = int(final_time)
    print(f'\n--Congratulations! You got : {final_score} score--')
    print("Game Over\n--Insert $1 coin to Play Again--")
    print(f"It took you {final_time} seconds to get the score")

    return final_score


if __name__ == '__main__':
    game()

closeInput = raw_input("Press ENTER to exit")