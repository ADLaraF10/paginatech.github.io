opcion = 1.0
while(opcion > 0 and opcion < 5):
    print("")
    print("Que punto desea ver")
    print("[1] punto 1")
    print("[2] punto 2")
    print("[3] punto 3")
    print("[4] punto 4")
    print("[0] salir")
    opcion = float(input("Eleccion:"))
    # -------------------------------  Sintaxis Básica y Operaciones Simples ------------------------------
    def punto1():
        # Declarar variables de diferentes tipos
        entero = 10
        flotante = 15.5
        cadena = "Hola Mundo"
    
        # Operaciones matemáticas simples
        suma = entero + flotante
        resta = flotante - entero
        multiplicacion = entero * 2
        division = flotante / 2
    
        # Concatenar cadenas de texto
        nombre = input("¿Cuál es tu nombre? ")
        print("Hola, " + nombre + "! Bienvenido al laboratorio.")
    
    # ---------------------------------------  Condicionales y Bucles -------------------------------------
    def punto2():
        # Condicionales: Determinar si un número es par o impar
        print("el numero es par o impar.")
        numero = int(input("Introduce un número: "))
        if numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")
    
        # Bucle for: Iterar sobre una lista e imprimir los cuadrados de los números
        print("Iterador de numeros.")
        numeros = [4, 6, 8, 9, 10]
        for n in numeros:
            print(f"El cuadrado de {n} es {n**2}")
    
    # ---------------------------------------  Listas y Diccionarios -------------------------------------
    def punto3():
        # Lista de nombres de estudiantes
        estudiantes = ["Juan", "Ana", "Luis"]
        for estudiante in estudiantes:
            print(f"Estudiante: {estudiante}")
    
        # Diccionario de información de contacto
        contactos = {
            "Juan": "juan@example.com",
            "Ana": "ana@example.com"
        }
        for clave, valor in contactos.items():
            print(f"Nombre: {clave}, Correo: {valor}")
    
        # Script para agregar elementos a una lista o actualizar un diccionario
        nuevo_estudiante = input("Introduce el nombre de un nuevo estudiante: ")
        estudiantes.append(nuevo_estudiante)
        print("Lista actualizada de estudiantes:", estudiantes)
    
        nuevo_contacto = input("Introduce un nombre para actualizar/agregar: ")
        nuevo_correo = input("Introduce el correo de este contacto: ")
        contactos[nuevo_contacto] = nuevo_correo
        print("Contactos actualizados:", contactos)
    
    # ----------------------------- Script de Resolución de Problemas Simples -------------------------------
    def punto4():
        # Calculadora básica
        def calculadora():
            print("Calculadora básica:")
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            operacion = input("Elige una operación (+, -, *, /): ")
        
            if operacion == "+":
                print(f"Resultado: {num1 + num2}")
            elif operacion == "-":
                print(f"Resultado: {num1 - num2}")
            elif operacion == "*":
                print(f"Resultado: {num1 * num2}")
            elif operacion == "/":
                if num2 != 0:
                    print(f"Resultado: {num1 / num2}")
                else:
                    print("Error: División por cero.")
            else:
                print("Operación no válida.")
        
        # Juego de adivinanza
        
        def adivinanza():
            import random
            numero_aleatorio = random.randint(1, 100)
            adivinanza = -1
            
            while adivinanza != numero_aleatorio:
                adivinanza = int(input("Adivina el número (entre 1 y 100): "))
                if adivinanza < numero_aleatorio:
                    print("Mayor...")
                elif adivinanza > numero_aleatorio:
                    print("Menor...")
                else:
                    print("¡Correcto! Adivinaste el número.")
        
        print("que ejercios quieres provar")
        print("[1] Calculadora")
        print("[2] Adivinanza")
        ejercio = int(input("escoja el numero de la opcion"))
        if(ejercio == 1):
            Calculadora()
        elif(ejercio == 2):
            Adivinanza()
    
    # ------------------------------------------ Menu ------------------------------------------------
    if(opcion == 1):
        punto1()
    elif(opcion == 2):
        punto2()
    elif(opcion == 3):
        punto3()
    elif(opcion == 4):
        punto4()