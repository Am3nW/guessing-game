import random
import pyfiglet
import sys
from tabulate import tabulate

nums = "123456789"
hidden_number = ''.join(random.sample(nums,4))
attempt_limit = 10
attempt_count = 0

print("Welcome to ATTEMPTS!\n")
print("Rules:")
print("- You need to guess a 4-digit number.")
print("- Digits range from 1 to 9 (no zero).")
print("- Each digit appears only once in the hidden number.\n")

attempt_history = []

while attempt_count < attempt_limit:
    attempt_count += 1
    print(f"Attempt {attempt_count} of {attempt_limit}.")
    attempt = input("ATTEMPT: ")

    if not attempt.isdigit() or len(attempt) != 4:
        print("Please enter a valid 4-digit integer.")
        continue

    if len(set(attempt)) != 4 or '0' in attempt:
        print("Digits must be unique and range from 1 to 9.")
        continue

    id_count = str(sum(1 for digit in attempt if digit in hidden_number))
    pos_count = str(sum(1 for i in range(4) if attempt[i] == hidden_number[i]))

    attempt_history.append([attempt, id_count, pos_count])

    att_his=tabulate(attempt_history,headers=["ATTEMPT","ID","POS"], tablefmt="grid")
    print(att_his)
    

    if attempt == hidden_number:
        sys.exit(pyfiglet.figlet_format("YOU WON", font='slant'))

        
print(f"The hidden number was {hidden_number}\n")
sys.exit(pyfiglet.figlet_format("YOU LOSE", font='slant'))

    

    



                


