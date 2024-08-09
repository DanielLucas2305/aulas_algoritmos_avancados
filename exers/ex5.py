num = int(input("Insira um numero para ter seu fatorial: "))
one = 1

for i in range(2, num + 1):
    one *= i

print('O fatorial é: ',one)

def fatorial(n):
    if n == 0:
        return 1
    else:
        n * fatorial(n-1)
        return print(n)
    
    
num2 = int(input("Insira um numero para ter seu fatorial com recursividade: "))

fatorial(num2)