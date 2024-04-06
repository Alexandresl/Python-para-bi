# Gere código Python que crie uma lista com os números entre 1 e 100 e então imprima os números pares, mas somente se o número for divisível por 4.

# # Cria a lista com os números entre 1 e 100
# numeros = list(range(1, 101))

# # Percorre a lista e verifica se o número é par e divisível por 4
# for numero in numeros:
#     if numero % 2 == 0 and numero % 4 == 0:
#         print(numero)

# Gere código Python que crie uma lista com os números entre 1 e 100 e então imprima os números pares, mas somente se o número for divisível por 4, usando list comprehension.


# Criar uma lista com números de 1 a 100
numeros = list(range(1, 101))

# Usar list comprehension para filtrar os números pares divisíveis por 4
numeros_pares_divisiveis_por_4 = [num for num in numeros if num % 2 == 0 and num % 4 == 0]

# Imprimir os números filtrados
print("Números pares divisíveis por 4 entre 1 e 100:")
print(numeros_pares_divisiveis_por_4)