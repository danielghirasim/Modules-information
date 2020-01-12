import sys

def helloworld(number):
    for x in range(int(number)):
        print('Hello World')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        number = sys.argv[1]
        helloworld(number)

