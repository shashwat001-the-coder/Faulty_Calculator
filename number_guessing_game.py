n=18
number_of_guesses=1
print("This is a number Guessing Game")
inputed_name=input("Enter your name:")
name=inputed_name.capitalize()
print("This game is limited to 9 times guesses")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number(between 0-100):"))
    if guess_number<18:
        print("You enter less number please input greater number.")
    elif guess_number>18:
        print("You enter greater number please input smaller number.")
    else:
        print("You won")
        print(name+" you took",number_of_guesses,"guess to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")