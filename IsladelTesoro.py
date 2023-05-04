print("Inicio")
print("bienvenido a tu isla, tu misión será encontrar el tesoro")
print("te encuentras dos caminos")
caminos = input("¿Derecha o izquierda?:")
if caminos == "izquierda":
    print("encuentras un río")
    rio = input("¿nadar o esperar?:")
    if rio == "esperar":
        print("aparece un castillo")
        castillo = input("¿entrar o esperar?:")
        if castillo == "entrar":
            print("hay muchas puertas de colores")
            puertas = input("¿Abres la puerta de que color?:")
            if puertas == "amarillo":
                print("haz Ganado")
            elif puertas == "rojo":
                print("eres quemado vivo game over")
            elif puertas == "azul":
                print("devorado por bestias game over")
            else:
                print("game over")
        else:
            print("Te cae un rayo game over")
    else:
        print("atacado por una tribu acuatica game over")
else:
    print("caiste en un agujero game over")
print("fin")