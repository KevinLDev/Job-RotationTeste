def fibonacci(num):
    a = 0
    b = 1
    while b < num:
        temp = b
        b = a + b
        a = temp
    if b == num:
        return f"{num} pertence à sequência de Fibonacci"
    else:
        return f"{num} não pertence à sequência de Fibonacci"
    
# Exemplo de uso:
print(fibonacci(21)) # 21 pertence à sequência de Fibonacci
print(fibonacci(22)) # 22 não pertence à sequência de Fibonacci
