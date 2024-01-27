
#Inicializar variable continuar
continuar = True

#Funcion para mostrar menu
def mostrarMenu():
    print("----Calculadora por Consola----\n"
          "Seleccione la operación: \n"
          "1. Suma (+)\n"
          "2. Resta (-)\n"
          "3. Multiplicación (*)\n"
          "4. División (/)\n"
          "5. Salir (Q)\n"
          "Ingrese la elección: ")

#Funcion para comprobar si la funcion es valida
def esOperacionValida(operacion):
    return operacion == "+" or operacion == "-" or operacion == "*" or operacion == "/"
    

#Funtion for doing operation
def realizarOperacion(operacion):
    try:
        num1 = float(input("Inserte el primer numero: "))
        num2 = float(input("Inserte el segundo numero: "))
    except ValueError:
        print("Los valores no son correctos")
        return

    #Diccionary for operations
    operaciones = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": None
    }

    try:
        operaciones["/"] = num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return

    resultado = operaciones.get(operacion)
    print("El resultado es:", resultado)


#Loop to make the operations
while(continuar==True):
    mostrarMenu()
    operacion = str(input())
    if (operacion =="Q" or operacion =="q"):
        print("--------FIN--------")
        continuar=False
    elif operacion in "+-*/":
        esOperacionValida(operacion)
        realizarOperacion(operacion)
            #Asking if continue
        temp = input("¿Quiere Continuar (S/N)")
        if (temp.upper()) == "S":
            continuar = True
        else:
            print("--------FIN--------")
            continuar = False   
    else:
        raise TypeError("Valor incorrecto")
    
  


    
    