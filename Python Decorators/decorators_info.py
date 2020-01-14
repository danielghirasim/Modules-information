# from functools import wraps
#
#
# # def decorator_function(original_function): # We pass in original_function as a arg
# #     def wrapper_function(): # We define the inner function also called Wrapper function
# #         print('This was printed before') # Everything here gets executed before our original_function
# #         return original_function() # After we execute what we wanted we then execute our original_function
# #     return wrapper_function # We return wrapper_function in an "unsolicited way"
# #
# #
# # @decorator_function # This is basically saying new_function = decorator_function(the_func_we_want_to_be_executed)
# # def hello_world():
# #     print("Hello World")
# #
# #
# # hello_world() # In the end we simply call our hello_world function which is basically new_func = decorator_function(hello_world)
# #
# # ### Some real-world examples ###
# #
# def logger_function(function_to_be_logged):
#     import logging
#     logging.basicConfig(filename=f'{function_to_be_logged.__name__}.log',
#                         level=logging.INFO)  # .__name__ gives us the name of the function
#     @wraps(function_to_be_logged)
#     def wrapper(*args, **kwargs):  # args = positional arguments , kwargs = keyword arguments (example below)
#         logging.info(
#             f'Ran with args: {args}\nkwargs: {kwargs}'
#         )
#         return function_to_be_logged(*args, **kwargs)
#
#     return wrapper
#
#
# #
# # @logger_function
# # def hello_world(msg):
# #     print(f'Hello {msg}')
# #
# # hello_world('world!')
# #
# # # Example of *arg - positional argument
# # hello_world(', this is a positional argument.')
# # # Example of **kwarg - keyword argument
# # hello_world(msg='This is a keyword argument.')
#
# def my_timer(orig_func):
#     import time  # Import time module
#     from time import sleep
#
#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         """We make a variable called to_be_timed otherwise we have to run the function
#            and that would print hello + {msg} again."""
#         t1 = time.time()  # Get's T1
#         sleep(0.2)
#         to_be_timed = orig_func(*args, **kwargs)
#         t2 = time.time() - t1  # t2 - t1 gives us the actual runtime of our function
#         print(f'{orig_func.__name__} ran in : {t2} sec')
#         return to_be_timed  # We return our newly made variable
#
#     return wrapper
#
#
# # new_funct = my_timer(logger_function(hello_world))
# @logger_function
# @my_timer
# def hello_world(msg):
#     print(f'Hello {msg}')
#
# hello_world('world!')

# Doing decorators with classes

class decorator_class():

    def __init__(self,original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('The call method executed this before my_timer()')
        return self.original_function(*args, **kwargs)

@decorator_class
def hello_world(msg):
    print(f'Hello {msg}')

hello_world('world!')