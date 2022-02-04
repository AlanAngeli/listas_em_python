""""
range

"""

li = list(range(0,100,8)) #de 0 a 100 em múltiplos de 8

lista = [0,1,2,3,4,5,6,7,8,9]

soma = 0
for valor in lista:
    soma = soma + valor #vai somar todos os números da lista

print("A soma de todos os números da lista é: ", soma)

lista2 = ["str", True, 10, -20.5]

print(type(lista2)) #escrevendo direto sem usar o comando for, vai mostrar que é do tipo list

for elemento in lista2:
    print("O tipo do elemento é",type(elemento), "e seu valor é", elemento)


