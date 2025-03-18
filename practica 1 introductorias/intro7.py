lista = []
lista_string=[]

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
    if num % 3 != 0:
        lista_string.append(str(num))   

#une los numeros con -
resultado = "-".join(lista_string)

print(resultado)