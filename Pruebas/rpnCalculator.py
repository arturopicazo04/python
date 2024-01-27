def rpn_calculator():  # Define una función llamada rpn_calculator.
    stack = []  # Crea una lista vacía llamada stack. Esta lista se usará como una pila para almacenar los números.

    while True:  # Inicia un bucle infinito.
        input_str = input("Ingrese la operación RPN (o 'q' para salir): ")  # Solicita al usuario que ingrese una operación RPN.

        if input_str.lower() == 'q':  # Si el usuario ingresa 'q', se rompe el bucle y se termina la función.
            break

        tokens = input_str.split()  # Divide la cadena de entrada en tokens. Cada token es un número o una operación.

        for token in tokens:  # Itera sobre cada token.
            if token in "+-*/":  # Si el token es una operación...
                if len(stack) < 2:  # ...y si no hay al menos dos números en la pila, imprime un error y rompe el bucle.
                    print("Error: no hay suficientes valores")
                    break

                num2 = stack.pop()  # Saca el último número de la pila y lo almacena en num2.
                num1 = stack.pop()  # Saca el siguiente número de la pila y lo almacena en num1.

                # Dependiendo de la operación, realiza la operación correspondiente con num1 y num2 y almacena el resultado en result.
                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                elif token == '/':
                    if num2 == 0:  # Si la operación es una división y num2 es 0, imprime un error y rompe el bucle.
                        print("Error: división por cero")
                        break
                    result = num1 / num2

                stack.append(result)  # Empuja el resultado de la operación a la pila.

            else:  # Si el token es un número...
                stack.append(float(token))  # ...convierte el token a un número flotante y lo empuja a la pila.

        # Si después de procesar todos los tokens hay exactamente un número en la pila, imprime ese número como el resultado.
        if len(stack) == 1:
            print("El resultado es: ", stack[0])
        else:  # Si no, imprime un error.
            print("Error: la operación no está completa")

rpn_calculator()  # Llama a la función rpn_calculator.