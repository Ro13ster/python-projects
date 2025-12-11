import random

def main():
    words = ["SIXTY", "SEVEN", "BALLS", "BUHHH", "SHAPT", "HOLLY", "WORDL", "LOSER", "LMFAO", "RYANN", "SAMII", "SPENC"]
    word_index = random.randint(0, len(words)-1)
    target_word = words[word_index]
    correct = False
    for i in range(6):
        print(f"You are on attempt {i + 1}")
        while True:
            guess = (input("Word: ").upper())
            if len(guess) != 5:
                print("Failure. Try again with a viable 5 letter word. Try again.")
            else:
                break
        for j in range(5):
            if guess[j] == target_word[j]:
                print(f"Same letter, Same position: {guess[j]}")
            elif guess[j] in target_word:
                print(f"Same letter, Wrong position: {guess[j]}")
            else:
                print(f"Not in word at all: {guess[j]}")
        if guess == target_word:
            correct = True
            print("Good job!")
            break
    if not correct:
        print(f"You lose! Correct word was {target_word}")

main()

