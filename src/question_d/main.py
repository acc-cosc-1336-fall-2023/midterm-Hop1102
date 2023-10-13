#add import
import question_d

def main():
    while True
        try:
            user_input = int(input("Enter a number(any other character will quit): "))
            if user_input <= 0:
                print("Please enter a positive integer.")
            else:
                result = get_sum_of_evens(user_input)
                print(f"The sum of even numbers to {user_input} is: {result}" )
        except ValueError:
            print("invalid entry. Please enter a number.")
            continue
        quit_choice = input("Do you wish to quit?(yes/no): ")
        if quit_choice.lower() == 'yes':
            break
        
    if __name__ == "__main__":
        main()
        

                
