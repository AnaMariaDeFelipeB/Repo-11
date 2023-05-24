# Punto 5

def crearMatrizUno (*args):  # Definimos función. (Permite al usuario crear matrices)
    global matrizUno  # Definimos variable global. 
    matrizUno = [] # Creamos lista vacia. (Donde ingresaremos los valores de la matriz)
    for fila in range(filaMatriz1): # Iteramos. (Vamos a generar la cantidad de filas)
        listafilamatriz1 = [] #Lista vacia. (Donde ingresaremos los valores de cada fila)
        for numero in range(columnaMatriz1): # Itera la longitud de la lista. 
            num : int = int(input("Ingrese número a la matriz número 1: ")) # Por cada iteración, va a preguntar un número. 
            listafilamatriz1.append(num) # Agrega el número dado a una lista. 
        matrizUno.append(listafilamatriz1) # Agrega la lista a la matriz principal. 
    
    for iterar in range(len(matrizUno)): # Recorre las filas de la matriz. 
        print(matrizUno[iterar]) # Imprime las filas. 

    return ("Matriz 1") # Duelve. 


def matrizSumaFila (*args):

    suma: int = 0 # Generemos variable. (Ira almacenando los datos de la suma)
    numerofila: int = int(input("Ingrese número de la FILA a SUMAR: ")) # Pedirá al usuario ingresar la fila que desea sumar. 
    if numerofila >= filaMatriz1: #Establece condición. (Si el valor de la fila ingresado es mayor o igual a las filas de la matriz)
        print("Error. La matriz ingresada anteriormente cuenta con un número menor de filas. Intentar nuevamente. ") # Si cumple la condición anterior, imprime. 
    else: # Si no la cumple, continua. 
        for columna in range(columnaMatriz1): # Ietera tantas columnas haya en la matriz. 
            variable = matrizUno[numerofila][columna] #Guarda el valor obtenido de la matriz. 
            suma += variable #Actualiza. (Va sumandose)
    return ("La suma es: " + str(suma)) # Devuelve

if __name__ == "__main__": # Permite inicializar la función. 
    filaMatriz1: int = int(input("Ingrese filas matriz 1: ")) # Pide valor.
    columnaMatriz1: int = int(input("Ingrese columnas matriz 1: ")) # Pide valor.
    print(crearMatrizUno(filaMatriz1, columnaMatriz1)) # Imprime función. 
    print(matrizSumaFila(filaMatriz1, columnaMatriz1)) # Imprime función. 