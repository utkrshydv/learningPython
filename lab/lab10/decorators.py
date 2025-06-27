# # # #functions are objects in python and can be passed through parameters

# # # #for eg: 
# # # #def f1():
# # # # print("f1 called")

# # # #def f2(f):
# # # # f()

# # # #f2(f1)
# # # #output -> f1 called



# # # def f1(func):
# # #   def wrapper():
# # #     print("Started")
# # #     func()
# # #     print("Ended")

# # #   return wrapper

# # # def f():
# # #   print("Hello")

# # # f1(f)() #calls the f1 func

# # # x = f1(f)
# # # x()   #calls the f1 func

# # # #instead of writing this again...we can just use decorators

# # # @f1
# # # def t():
# # #   print("Hello from t")

# # # #now everytime t is called, f1 is also run as t as the argument

# # # def f1(func):
# # #   def wrapper(*args, **kwargs): #if arguments are being passed
# # #     print("Started")
# # #     func(*args, **kwargs)
# # #     print("Ended")
# # #   return wrapper

# # # @f1
# # # def f(a, b=9):
# # #   print(a, b)

# # # f("Hi!")

# # # #output->
# # # # Started
# # # # Hi! 9
# # # # Ended


# # # to return a value from function

# # # def f1(func):
# # #   def wrapper(*args, **kwargs):
# # #     print("Started")
# # #     val = func(*args, **kwargs)
# # #     print("Ended")
# # #     return val
# # #   return wrapper

# # # @f1
# # # def add(x, y):
# # #   return x + y

# # # print(add(4, 5))

# # #output:
# # #Started
# # #Ended
# # #9


# # #decorators can be used on more than one function 

# # #eg usecase -> check timetaken by different algorithms

# # import time

# # def timer(func):
# #   def wrapper():
# #     before = this.time()
# #     func()
# #     print("func took: ", time.time() - before, "seconds")

# #   return wrapper

# # @timer
# # def run():
# #   time.sleep(2)

# # run()


# #eg usecase : log

# import datetime

# def log(func):
#   def wrapper(*args, **kwargs):
#     with open("log.txt", "a") as f:
#       f.write("Called function with " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n" )
#     val = func(*args, **kwargs)
#     return val
  
#   return wrapper

# @log
# def run(a, b, c=9):
#   print(a+b+c)

# run(1, 3, c=9)

#Decorators work with classes as well, not just functions. Also worth adding:

