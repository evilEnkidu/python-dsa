import time 
def tictoc(print_numbers_version_two):
      def wrapper():
            t1 = time.time()
            print_numbers_version_two()
            t2 = time.time() - t1
            print(f"{print_numbers_version_two.__name__} ran in {t2} seconds")
      return wrapper

@tictoc
def print_numbers_version_two():
      number = 2
      while number <= 100:
            print(number)
            number += 2

print_numbers_version_two()