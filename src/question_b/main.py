#add import

from get_bonus_pay import get_bonus_pay

def main():
    sales = float(input('Enter a sales amount: '))

    bonus = get_bonus_pay(sales)

    print(f"The bonus pay amount is: {bonus}")

if __name__ == '__main__':
    main()
