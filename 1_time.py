import time 
def tictoc(print_numbers_version_one):
    def wrapper():
        t1 = time.time()
        print_numbers_version_one()
        t2 = time.time() - t1
        print(f"{print_numbers_version_one.__name__} ran in {t2} seconds")
    return wrapper

@tictoc
def print_numbers_version_one():
    number = 2
    while number <= 100:
        if number % 2 == 0:
            print(number)
        number += 1

print_numbers_version_one()
