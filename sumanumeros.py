#recibe una lista de números y calcula la suma
numeros = int(input("ingrese la cantidad de números (,):"))
sumatoria = 0
for i in range(numeros):
    n=int(input("ingrese el número:"))
    sumatoria=sumatoria + n
print(sumatoria)
