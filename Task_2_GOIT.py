import random

def get_numbers_ticket(min, max, quantity):
    set_of_numbers = []
    if min >= 1 and max <= 1000:
        for n in range(min, max):
            set_of_numbers.append(n)
        quantity = random.sample(set_of_numbers, quantity)
        sort_quantity = sorted(quantity)
        return sort_quantity
    else:
        print("Plaese enter correct data")
        return set_of_numbers
        

result = get_numbers_ticket(1,36,5)
print(result)