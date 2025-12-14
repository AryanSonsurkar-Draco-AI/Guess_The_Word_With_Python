import random

def random_word():
    try:
        with open("words.txt", "r") as file:
            clean_words = []

            for line in file:
                cleaned = line.strip()
                if cleaned:
                    clean_words.append(cleaned)

            secret_word = random.choice(clean_words)
            return secret_word

    except FileNotFoundError:
        print("File Not Found.")
        return None


def main():
    secret_word = random_word()
    if not secret_word:
        return

    hidden_word = ["_"] * len(secret_word)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Guess the Word (Mini Hangman)")
    print("You have", attempts, "attempts")

    while attempts > 0 and "_" in hidden_word:
        print("\nWord:", " ".join(hidden_word))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print("Attempts left:", attempts)

        # STEP 4: INPUT VALIDATION LOOP
        while True:
            guess = input("Enter one letter: ").lower()

            if len(guess) != 1:
                print("Enter only ONE letter.")
            elif not guess.isalpha():
                print("Only alphabets are allowed.")
            elif guess in guessed_letters:
                print("You already guessed this letter.")
            else:
                break

        guessed_letters.add(guess)

        # Reveal logic
        if guess in secret_word:
            for index in range(len(secret_word)):
                if secret_word[index] == guess:
                    hidden_word[index] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    # Game result
    if "_" not in hidden_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
    else:
        print("\n❌ You lost! The word was:", secret_word)


if __name__ == "__main__":
    main()
