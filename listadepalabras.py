#utilizando for y if este programa recibe palabras y muestra las que empiezan por cierta letra
cantidad = int(input("ingrese la cantidad de palabras:"))
listap = []
for i in range(cantidad):
    palabra=str(input("ingrese una palabra:"))
    listap.append(palabra)
inicial = str(input("letra inicial:"))

palabracorrecta = []
for palabra in listap:
    if palabra.startswith(inicial):
        palabracorrecta.append(palabra)
print(palabracorrecta)