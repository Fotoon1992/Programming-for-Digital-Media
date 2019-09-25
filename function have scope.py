def set_a():
    a = 10
    print('The value of a:', a)
    set_a()
    a = 20
    print('Initially, the value os a:', a)
    set_a()
    print('Initially, the value of a:', a)
def scoped(first, second):
    first = 10
    second = 11
    third = 12
    third = second + second - first
    return third
scoped(2, 4)
first
second
third