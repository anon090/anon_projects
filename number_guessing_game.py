import random 
from colorama import Fore,Style
def number_guessing_game(max_attempt):
    random_number = random.randint(1, 100)
    print(random_number)
    attempts = 0
    while attempts<=max_attempt:
        guess = input("Guess a number between 1 and 100: ")
        guess=guess.strip()
        if len(guess)>0:
            guess=int(guess)
            attempts += 1

            if guess == random_number:
                print(f"{Fore.GREEN+Style.BRIGHT}Congratulations! You guessed the number in {attempts} attempts.{Style.RESET_ALL}")
                break
            elif guess < random_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        else:
            attempts+=1
    else:
        print("you can do it next time be confident")

try:
    chk='y'
    while chk=='y':
        print(f"1.Easy Level\n2.Medium Level\n3.Hard Level")
        choice=int(input(Fore.YELLOW+"Enter your choice :"+Style.RESET_ALL))
        match(choice):
            case 1:
                number_guessing_game(60)
            case 2:
                number_guessing_game(40)
            case 3:
                number_guessing_game(20)
            case _:
                print(f"{Fore.RED+Style.BRIGHT}Choice is Invalid!Please Enter a Valid Choice{Style.RESET_ALL}")
        chk=input(f"{Fore.YELLOW+Style.BRIGHT}you want to try again say (yes for press y and no for press n):{Style.RESET_ALL}").lower().strip()
except ValueError:
    print(Fore.RED+Style.BRIGHT+"Error: Please Enter a Valid Value"+Style.RESET_ALL)
except Exception as e:
    print(f"{Fore.RED+Style.BRIGHT+"Error :"+Style.RESET_ALL} {e}")