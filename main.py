import random
import drawings
from termcolor import colored, cprint

print("""Howdy Pard'ner, Welcome to Hangman
Here are the rules:
1. You have 6 guesses
2. You can choose a letter to fill out the word
3. Or you can take a whack at the word itself
4. Every wrong answer adds up and helps MURDER the hangman (which is bad)
5. So try to guess that word!""")

words= ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar',
         'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat',
         'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt',
         'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven',
         'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider',
         'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 
         'wombat', 'zebra']


secret_word= random.choice(words)
display = len(secret_word)* "_"
count = 0
list= []

for items in secret_word:
    list.append("_")

while count <=7:

    if '_' not in list:
        print("youve won! You saved me!!!!!(But what kind of life did you leave me with?!?!?!)")
        break
    elif count == 6:
        cprint(f"you've lost! You killed me!!!!!!! the word was {secret_word} damnit!", "white", "on_red")
        
        break
    else:
        user_choice= input("Guess a letter or the word? " )
        if user_choice == secret_word:
            print("You've won! You saved me!!!!!! (But what kind of life did you leave me with?!?!?!)")
            break 
        
        elif len(user_choice) == 1:


            if user_choice in secret_word:
                char_count = 0

                while char_count < len(secret_word):    
                    if secret_word[char_count] == user_choice:
                        list[char_count] = user_choice
                        char_count +=1
                    else:
                        char_count +=1
            else:
                count +=1                        
        else:
              count+=1              
                   
    
    print(drawings.image(count)) 
    print("".join(list))     
   