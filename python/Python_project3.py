                    # Hangman Game #

import random
lives = 6
word =["vaishnavi", "apple", "attitude", "resolution", "attachment"
      ,"people", "cricket", "python", "hangman", "eligant", "nice"
      , "beautiful", "project"]
chosen_word = random.choice(word)
print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over: 
    guessed_letter = input("Guess a letter: ").lower()
    for j in range(len(chosen_word)):
        i = chosen_word[j]
        if i == guessed_letter:
            display[j] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You lose!!")
    if '_' not in display:
        game_over = True
        print("Yoe win")
    # print(hangman_stages.stages[lives])

