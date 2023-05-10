import time

def timer(func):
   """A decorator that prints how long a function took to run."""
    # Define the wrapper function to return.
    def wrapper(*args, **kwargs):
      # when wrapper is called, get the current time
      t_start = time.time()
      # call the decorated function and store the result
      result = func(*args, **kwargs)
      # get the total time it took to run, and print
      t_total = time.time() - t_start
      print('{} took {}s'.format(func.__name__, t_total))
      return result
    return wrapper
            
def memoize(func):
   """Store the results of the decorated function for fast lookup"""
   cache = {}
   def wrapper(*args, **kwargs):
      if(args, kwargs) not in cache:
           cache[(args, kwargs)] = func(*args, **kwargs)
   return wrapper
