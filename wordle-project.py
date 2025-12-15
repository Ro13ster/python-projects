import random

def main():
    file = open("words.txt", "r")
    content = file.read()
    words = content.split('\n')
    file.close()
    word_index = random.randint(0, len(words)-1)
    target_word = words[word_index]
    correct = False
    for i in range(6):
        print(f"You are on attempt {i + 1}")
        results = ""
        while True:
            guess = (input("Word: ").upper())
            if len(guess) != len(target_word):
                print(f"Failure. Try again with a viable {len(target_word)} letter word. Try again.")
            else:
                break
        for j in range(len(target_word)):
            if guess[j] == target_word[j]:
                results = results + f"\033[32m[{guess[j]}]\033[0m"
            elif guess[j] in target_word:
                results = results + f"\033[33m[{guess[j]}]\033[0m"
            else:
                results = results + (f"\033[90m[{guess[j]}]\033[0m")
        print(results)
        if guess == target_word:
            correct = True
            print("Good job!")
            break
    if not correct:
        print(f"You lose! Correct word was {target_word}")

main()