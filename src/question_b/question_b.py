#write functions here, don't add input('') statements here!

def get_bonus_pay(sales):
    if sales < 0 or sales > 1999:
        return 'Invalid'
    elif sales >= 1500:
        return sales * 0.08
    elif sales >= 1000:
        return sales * 0.07
    elif sales >= 500:
        return 0.06
    else:
        return sales * 0.05