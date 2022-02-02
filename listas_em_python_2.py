"""

append, insert, pop, del, clear, extend, +
min, max
range

"""
#índice   0   1   2   3   4
lista = ["A","B","C","D","E"]
print(lista[0:3]) #mostrará o índice 0 até o 2
print(lista[::2])#pula de dois em dois
print(lista[::-2])#pula dois de trás pra frente
print()

################################################

li1 = [1,2,3]
li2 = [4,5,6]
li3 = li1 + li2

print(li1)
print(li2)
print(li3)
print()
li4 = ["a","b","c"]
li5 = ["d","e","f"]
li4.extend(li5) #usa-se o extend para emendar a lista 5 na 4
li5.append("g") #ou pode ser usado extende também: li5.extend("g")
print(li4)
print(li5)
print(li4[3])
print(li5[2])
print()
li4.insert(1,"a2")
print(li4)
li4.insert(3,"c2")
print(li4)
li4.insert(5,"d2")
print(li4)


