import random
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
#arma una lista random que se puede repetir , agrupando la pregunta lass respuestas y la respuesta correcta . solo 3 de todas las que hay
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

puntos = 0 
# El usuario deberá contestar 3 preguntas
# recorre el for y apruepa en cada variable lo que le corresponde  
for question, answer_options, correct_answer_index in questions_to_ask:    

    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answer_options):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):        
        user_answer = input("Respuesta: ")
        if user_answer in ["1","2","3","4"]:
            user_answer= int(user_answer)-1
        else:
            print("Respuesta no Valida")
            exit(1)
        #se fija si la respuesta es correcta                
        if user_answer == correct_answer_index:
            puntos += 1
            print("¡Correcto!")
            break
        else:
           puntos -= 0.5  
           print("¡es Incorrecto!")   
    else:
        # Si el usuario no responde correctamente después de 2 intentos,  se muestra la respuesta correcta        
        print("Incorrecto. La respuesta correcta es:")
        print(answer_options[correct_answer_index])
        # Se imprime un blanco al final de la pregunta
        print()
#para que no muestre puntos negativos , si el resultado es menor a 0 te muestra cero             
if puntos < 0 :
    print("obtuvo 0 puntos")
else:
    print(f"obtuvo {puntos} puntos")