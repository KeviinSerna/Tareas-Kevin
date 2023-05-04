#usando for este programa imprime una tabla de multiplicar
tabla = int(input("¿Que tabla quieres conocer?:"))
for i in range(1, 11):
    respuesta = tabla * i
    print(tabla,"x",i,"=",respuesta)
    