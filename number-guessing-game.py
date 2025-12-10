import random

def main():
    while True:
        number = random.randint(1, 100)
        attempts = 0
        while True:
            attempts += 1
            print(f"You are on attempt number {attempts}")
            guess = int(input("Number: "))
            if (guess > number):
                print("Too high")
            elif(guess < number):
                print("too low")
            else:
                print (f"CORRECT! You found the right number in {attempts} attempts!")
                break
        print("Want to play again? Y or y for yes. N or n for no.")

        user_input = input("Input: ")
        if (user_input == 'Y' or user_input == 'y'):
            continue
        elif(user_input == 'N' or user_input == 'n'):
            break
             
main() 