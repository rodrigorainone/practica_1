lista = []

while True:
    try:
        entrada = input('ingrese un numero :  ')
        #si escribe salir deja de cargar numeros en la lista
        if entrada.lower() == "salir":
            break
        numeros = int(entrada)
        lista.append(numeros)
    except ValueError:
            print("entrada invalida ingrese numeros")

for num in lista:
    #si es un numero negativo deja de imprimir
    if num < 0:
        break
    print(num)