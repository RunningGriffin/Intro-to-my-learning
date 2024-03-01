import random

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def main():
    # Replace 'wordlist.txt' with the path to your word list file
    word_list = load_words('wordle\words.txt')

    # Initialize variables
    max_attempts = 6
    previous_guesses = set()
    possible_list = []

    correct_letters = [None, None, None, None, None]

    for attempt in range(max_attempts):
        guess = input('Make a Guess ')
        print(f"Attempt {attempt + 1}")
        done = False
        correct_positions = list()

        while not done:
        # Get user feedback (correct letters in correct positions)
            correct_position_index = int(input("Correct position index: (6 for done) "))
            if correct_position_index == 6:
                done = True
            else:
                correct_letters[correct_position_index] = guess[correct_position_index]
                correct_positions.append(correct_position_index)

        print(correct_letters)
        print(correct_positions)


        counter = 0
        for index in correct_positions:
            counter += 1
            if counter == 1:
                for word in word_list:
                    if word[index] == guess[index]:
                        possible_list.append(word)
            else:
                while index > len(possible_list):
                    if word[index] != guess[index]:
                        possible_list.remove(word)


        print(possible_list)



if __name__ == "__main__":
    main()




