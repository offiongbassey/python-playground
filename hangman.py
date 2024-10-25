import random

word = ["python", "java", "php", "javascript"]
choosen_word = random.choice(word)
word_display = ['_' for _ in choosen_word]
attempts = 8
while attempts > 0 and '_' in word_display:
    print(' '.join(word_display))
    guess = input("Guess the letter of the choosen word")
    if guess in choosen_word:
        for index, letter in enumerate(choosen_word):
            if guess == letter:
                word_display[index] = guess
    else:
        attempts -= 1
        print(f"Wrong letter choosen, you have {attempts} attempts left\n")

if '_' not in word_display:
    print(f"Congrats, you got it correctly. The word is {' '.join(choosen_word)}")
else:
    print(f"Sorry, you failed. The choosen word is {' '.join(choosen_word)}")