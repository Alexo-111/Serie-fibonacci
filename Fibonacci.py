N = 200


def fib(index):

    # Caso base
    if index == 1 or index == 2:
        return 1

    # Caso recursivo
    else:
        return fib(index - 1) + fib(index - 2)


# Mostrar la secuencia desde 1 hasta N
for i in range(1, N + 1):
    print("Índice", i, "=", fib(i))


	
