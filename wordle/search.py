import random

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def main():
    # Replace 'wordlist.txt' with the path to your word list file
    word_list = load_words('words.txt')

    # Initialize variables
    max_attempts = 6
    previous_guesses = set()
    possible_list = []

    for attempt in range(max_attempts):
        guess = input('Make a Guess ')
        print(f"Attempt {attempt + 1}")
        done = False
        correct_positions = [None]
        while not done:
        # Get user feedback (correct letters in correct positions)
            correct_position_index = int(input("Correct position index: (6 for done) "))
            if correct_position_index == 6:
                done = True
            else:
                correct_positions.append(correct_position_index)

        done = False
        invalid_words = ['6']
        while not done:
        # Get user feedback (correct letters in correct positions)
            invalid_word = input("invalid letters? (6 for done) ")
            if invalid_word == '6':
                done = True
            else:
                invalid_words.append(invalid_word)

        sentinal = False
        for word in word_list:
            for index in correct_positions:
                for invalid in invalid_words:
                    if invalid in word:
                        sentinal = True
            if word[index] == guess[index] and sentinal == False:
                possible_list.append(word)
        
        print(possible_list)

    print("Out of attempts. Wordle not solved.")

if __name__ == "__main__":
    main()




