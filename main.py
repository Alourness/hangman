word = "python"
guessed = []
lives = 6
while True: 
 display = ""
 for letter in word:
    if letter in guessed:
     display = display + letter + " "
    else:
     display = display + "_ "
 print(display)
 print(f"Lives: {lives}")
 if "_" not in display: 
    print("You found it!")
    break 
 if lives == 0:
    print("You lost!")
    break
 guess = input("Guess a letter: ").lower()
 guessed.append(guess)

 if guess in word:
    print("Yes")
 else:
    lives = lives - 1
    print("No!")