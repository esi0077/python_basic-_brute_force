import random
import time
import string

# Load the word list from the file
with open('passwordlist.txt', 'r') as file:
    word_list = [line.strip() for line in file.readlines()]

# Get passcode input from user
passcode = input("Enter passcode: ")

def bot_guess_passcode(passcode):
    possible_characters = string.ascii_letters + string.digits + string.punctuation + ' '
    attempt_count = 0  # Initialize the attempt counter
    
    # Start timing
    start_time = time.time()
    
    # Check if the passcode is in the word list
    if passcode in word_list:
        print(f"Passcode '{passcode}' found in the word list.")
        attempt_count += 1  # Count this as one attempt
    else:
        print(f"Passcode '{passcode}' not found in the word list. Starting character-based guessing...")
        guessed_passcode = [''] * len(passcode)
        
        while True:
            for i in range(len(passcode)):
                while guessed_passcode[i] != passcode[i]:
                    bot_char_guess = random.choice(possible_characters)
                    attempt_count += 1  # Increment attempt count for character guess
                    
                    print(f"| Bot is guessing character for position {i+1}: {bot_char_guess}")
                    
                    if bot_char_guess == passcode[i]:
                        guessed_passcode[i] = bot_char_guess
                        print(f"Correct character guessed: {bot_char_guess}")
                    else:
                        print(f"Incorrect character at position {i+1}. Trying again.")
                
            guessed_string = ''.join(guessed_passcode)
            print(f"Current guessed passcode: {guessed_string}")
            
            if guessed_string == passcode:
                print(f"Wow, the bot got the entire passcode!")
                break
            else:
                print("Bot is still trying to guess the passcode...")
    
    # End timing
    end_time = time.time()
    time_taken = end_time - start_time
    
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Total attempts: {attempt_count} attempts")

# Run the bot
bot_guess_passcode(passcode)
