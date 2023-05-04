#con ciclo for, este programa pide dos listas de números y suma las que están en la misma posición
cantidad = int(input("ingrese la cantidad de números de las listas:"))
lista1 = []
lista2 = []

for i in range(cantidad):
    num1= int(input("ingrese un número de lista1:"))
    lista1.append(num1)

for i in range(cantidad):
    num2= int(input("ingrese un número de lista2:"))
    lista2.append(num2)

resultado = []

for i in range(len(lista1)):
    suma=lista1[i]+lista2[i]
    resultado.append(suma)
print(resultado)