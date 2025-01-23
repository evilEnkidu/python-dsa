def time(function):
      def wrapper():
            import time
            t1 = time.time()
            function()
            t2 = time.time() - t1
            print(f"{function.__name__} ran in {t2} seconds")
      return wrapper

@time
def delete_first_from_list():
      my_list = [1, 2, 3, 4, 5]
      del my_list[0]
      return my_list

@time
def delete_last_from_list():
      my_list = [1, 2, 3, 4, 5]
      del my_list[-1]
      return my_list

delete_last_from_list()
