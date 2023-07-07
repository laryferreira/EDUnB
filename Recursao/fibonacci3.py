def fibonacci(n, count):
    count[n] += 1 #incrementa em 1 o valor de n na lista
    #casos base = 1º regra recursão!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1, count) + fibonacci(n-2, count)

n = int(input())

count = [0] * (n+1) #lista vazia
fibonacci_fim = fibonacci(n, count)

print(f"fibonacci({n}) = {fibonacci_fim}.")
for i in range(n+1):
    print(f"{count[i]} chamada(s) a fibonacci({i}).")
