inventario = { }

salir = True

while salir :
    print()
    print()
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Mostrar")
    print("4. Salir")
    print()
    print()

    #verifica que la elecccion sea valida
    while True:
        try:
            user_entrada = int(input ("elige una opcion : "))            
            if  (1 <= user_entrada<= 4):
                break 
            else:
                print("Respuesta no válida")   
                print() 
                print()  
        except ValueError:
            print("Respuesta no válida")   
            print() 
            print()  

    match user_entrada:
        case 1:                        
            print("agregar")
            print()
            nombre_producto=input("escriba el nombre del producto  :  ")
            #verifica que solo se ingrese un numero
            while True:
                try:
                    cantidad_producto=int(input("escriba la cantidad  :  "))    
                    break         
                except ValueError:
                    print("Respuesta no válida escriba un numero" )     
            #si no existe en el inventario lo agrega si existe , le suma la cantidad existente con la ingresada
            if not nombre_producto in inventario:
                inventario[nombre_producto]=cantidad_producto
            else:
                inventario[nombre_producto]+=cantidad_producto
        case 2:
            print("eliminar")
            print()
            nombre_producto=input("escriba el nombre del producto a eliminar  :  ")
             #si no existe en el inventario avisa que no se encuentra , si esta lo elimina
            if not nombre_producto in inventario:
                print("el producto no se encuentra en el inventario")
            else:
                del inventario[nombre_producto]
        case 3:
            print("mostrar")
            print()
            print()
            print(inventario)
            print()
            print()
        case 4:
            print("salir")
            print()
            salir = False
        case _:
            print("No es ninguno de los anteriores")
            print()

