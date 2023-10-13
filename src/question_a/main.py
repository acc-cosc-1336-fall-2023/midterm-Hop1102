#add import\

import get_random_number() 

def main():
    while True:
        random_number = get_random_number() 
        user_guess = int(input('Gues a number between 1 and 5:'))

        if user_guess == random_number:
            print(f'Congratulationms! The number was ({random_number})') 
        else:
            print(f'Sorry thats wrong, the correct number was {random_number}')

        play_again = input("Want to try again?(yes/no):")
        if play_again.lower() != 'yes':
            break

    if __name__ == "__main__":
        main()
