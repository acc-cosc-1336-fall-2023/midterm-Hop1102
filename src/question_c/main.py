#add import

def main():
    while True:
        try:
            user_input = int(input('Enter a number(1-7). Any other number will exit'))
            if user_input < 1 or user_input > 7:
                print('PLease enter a number between 1 and 7.')
            else:
                result = get_day_of_week(user_input)
                print(f'The corresponding day of the week is: {result}')
        except ValueError:
            print('Invalid input. Please enter a number between 1-7.')
            continue

        quit = input("Do you want to quit?(yes/no): ")
        if quit.lower() == 'yes':
            break

if __name__ == '__main__':
    main()
