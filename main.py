word = "python"
guessed = []
while True: 
 display = ""
 for letter in word:
    if letter in guessed:
     display = display + letter + " "
    else:
     display = display + "_ "
 print(display)
 if "_" not in display: 
    print("You found it!")
    break 
 guess = input("Guess a letter: ").lower()
 guessed.append(guess)
