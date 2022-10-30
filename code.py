
# importing different files into code
import random
from art import logo,stages
from word_list import words

# printing the game logo and taking two parameters which iterates contiously until the game is finished
print(logo)
game_is_finished = False
lives= len(stages)-1

# generating a random word to play the game
choosen_word = random.choice(words)
word_length=len(choosen_word)

# creating a list of size of the word generated and making the entire list as blank spaces
user_word=[]
for _ in range(word_length):
    user_word+= "_"

# code
# taking input from the user
while not game_is_finished:
    user_letter=input("Guess a letter: ").lower()

# if the input matches with is appropriate position, replacing the letter with blank.
    for position in range(word_length):
        letter=choosen_word[position]
        if letter==user_letter:
            user_word[position]=letter
    print(user_word)

# if user input doesnt match any letter in the word, the user will loose 1 life, if the user looses all lives the game ends.
    if user_letter not in choosen_word:
        print(f"You guessed {user_letter}, that's not in the word. you loose a life.")
        lives-=1
        print(stages[lives])
        if lives==0:
            game_is_finished=True
            print("You lose")

# if the blanks got filled with letters the game will be completed
    if not "_" in user_word:
        game_is_finished=True
        print("You win!!")


