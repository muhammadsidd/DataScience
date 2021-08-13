


def fib (pos):
    
    n = 0
    n1 =1

    index = 0

    if pos == 1 :
        print(n)
    
    while index < pos:
        print(n)
        temp = n + n1
        n = n1
        n1 = temp

        index = index + 1

x = fib(7)