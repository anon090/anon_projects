import os  # To clear the terminal screen
from random import randint  # To generate random numbers for password guessing
from time import time  # To measure the time it takes to run the code

# Start time tracking
start_time = time()  # Records the start time of the execution

# Prompt the user to enter a password to be "cracked"
input_password = input("Enter a Password :")  # Takes input from the user for the target password

# Define the list of characters to use for password cracking (lowercase letters + digits)
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
       'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
       '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', 
       '?', '/', '~', '`']

# Initialize an empty string that will represent the "cracked" password
pw = ''

# Start a loop that continues until the generated password matches the input password
while(pw != input_password):
    pw = ''  # Reset the generated password on each iteration
    for letter in range(len(input_password)):  # Loop over each character of the input password
        # Randomly pick a character from the 'pwd' list to guess the current character of the password
        guess_pwd = pwd[randint(0, len(pwd) - 1)]  # randint(0, len(pwd) - 1) gives a random number between 0 and len(pwd) - 1 (inclusive)
        
        # Build the guessed password incrementally by adding each new character at the front
        pw = str(guess_pwd) + str(pw)
        
        # Print the current guessed password so far
        print(pw)
        print("Cracking password... please wait")
        
        # Clear the terminal screen to show only the latest guess
        os.system('cls')  # 'cls' works for Windows, use 'clear' for Linux/Mac
        
# Once the password is cracked, display the guessed password
print("Your password: ", pw)

# Record the end time after the password is successfully cracked
end_time = time()

# Calculate and display the execution time by subtracting the start time from the end time
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.5f} seconds")  # Prints the time it took in seconds


# Important Note For Future
# 1) Multithreading/Parallelism: If you want to improve performance for longer passwords, consider using parallel computing or multi-threading to check multiple password combinations simultaneously.

#Important Notes:
#Brute Force Approach: This method is highly inefficient for cracking passwords longer than a few characters. For larger passwords or more complex character sets, it would take an impractically long time to complete.