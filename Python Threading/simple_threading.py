import time, threading

print('Program started')

msg = 'Wake up Neo...'
def say_this(msg):
    time.sleep(2)
    print(msg)


thread_func = threading.Thread(target=say_this, args=[msg])
thread_func.start()

print('Program ended')