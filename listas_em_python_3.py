"""

append, insert, pop, del, clear, extend, +
min, max
range

"""
lista = [0,1,2,4]
print(lista)
lista.insert(0,-1) #será inserido o valor -1 na lista
print(lista)
lista.insert(4,3)#será inserido o valor 3 na lista
print(lista)
lista.pop() #remove o último índice
print(lista)
print()
#índice = 0 1 2 3 4 5 6 7 8
lista2 = [1,2,3,4,5,6,7,8,9]
print(lista2)
lista2.insert(9,10)
print(lista2)
del(lista2[3:5]) #deleta do índice 3 até o 4, já que o último não conta
print(lista2)
print()
print(max(lista2)) #maior valor da lista
print(min(lista2)) #menos valor da lista
