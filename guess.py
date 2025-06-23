def get_unique_letters(word):
    """Returns a string of unique letters in the word."""
    unique = ""
    for ch in word:
        if ch not in unique:
            unique += ch
    return unique

def prompt_word():
    """Prompts the user to input a word to be guessed."""
    return str(input("\nEnter a guess word (blank to quit): "))

def prompt_letter():
    """Prompts the user for a single letter guess."""
    letter = str(input("\nEnter a guess letter (blank to quit): "))
    while len(letter) > 1:
        print("\t> Only enter a single letter")
        letter = str(input("\nEnter a guess letter (blank to quit): "))
    return letter

def play_game(word):
    """Main guessing loop for the game."""
    matched_guesses = ""
    unmatched_guesses = ""
    guessed_letters = ""
    number_guesses = 0
    finished = False

    unique_letters = get_unique_letters(word)

    while not finished:
        letter_guess = prompt_letter()

        # If the user enters a blank guess, exit the loop
        if len(letter_guess) == 0:
            break

        # Check if the letter was already guessed
        if letter_guess in guessed_letters:
            if letter_guess in unique_letters:
                print("\t>", letter_guess, "already guessed and found")
            else:
                print("\t>", letter_guess, "already guessed and not found")
        else:
            # Check if the guess is correct
            if letter_guess in unique_letters:
                print("\t>", letter_guess, "found")
                matched_guesses += letter_guess
            else:
                print("\t>", letter_guess, "not found")
                unmatched_guesses += letter_guess

        # Increment the guess counter
        number_guesses += 1

        # Add the guessed letter to the list of guessed letters if not already present
        if letter_guess not in guessed_letters:
            guessed_letters += letter_guess

        # Display all guessed letters so far
        print("\t> Guesses so far:", guessed_letters)

        # Check if all unique letters have been guessed
        finished = all(l in guessed_letters for l in unique_letters)

    # If the game is finished, display the results
    if finished:
        print("\t> All letters found")
        print()
        print("======== Results ========")
        print(f"Word:\t\t{word}")
        print(f"Matched:\t{matched_guesses}")
        if len(unmatched_guesses) == 0:
            unmatched_guesses = "(None)"
        print(f"Unmatched:\t{unmatched_guesses}")
        print(f"Guesses:\t{number_guesses}\n")

def main():
    # Prompt the user to input a word to be guessed
    word = prompt_word()
    if len(word) != 0:
        play_game(word)

if __name__ == "__main__":
    main()
