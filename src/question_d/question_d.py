#write functions here, don't add input('') statements here!

def get_sum_of_evens(num):
    return sum(i for i in range(2, num+1, 2))
    