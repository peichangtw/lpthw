# * asterisk
def print_2(*args):
#arg1, arg2 = args
    print(f'arg1 {arg1}, arg2 {arg2}')

def print_2_again(arg1, arg2):
    print(f'arg1 {arg1}, arg2 {arg2}')

def print_1(arg1):
    print(f'arg1 {arg1}')

def print_none():
    print('nothing')

print_2('a','b')
print_2_again('a','b')
print_1('a')
print_none()