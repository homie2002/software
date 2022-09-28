fib1 = 0
fib2 = 1

n = input("Номер елемнту ряду Фібоначі: ")
n = int(n)

print(fib1, fib2, end=' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

print('\n'"Елемент під номером",n,"має значення",fib2 )