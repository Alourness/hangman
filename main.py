word = "python"
guessed = [] 
guess = input("Guess a letter: ").lower() # NEW
guessed.append(guess) 
display = ""
for letter in word:
    if letter in guessed: 
     display = display + letter + " "
    else: 
     display = display + "_ "
    print(display)  