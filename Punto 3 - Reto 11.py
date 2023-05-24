# Punto 3 

def crearMatrizUno (*args):  # Definimos función. (Permite al usuario crear matrices)
    global matrizUno  # Definimos variable global. 
    matrizUno = [] # Creamos lista vacia. (Donde ingresaremos los valores de la matriz)
    for fila in range(filaMatriz1): # Iteramos. (Vamos a generar la cantidad de filas)
        listafilamatriz1 = [] #Lista vacia. (Donde ingresaremos los valores de cada fila)
        for numero in range (columnaMatriz1): # Itera la longitud de la lista. 
            num : int = int(input("Ingrese número a la matriz número 1: ")) # Por cada iteración, va a preguntar un número. 
            listafilamatriz1.append(num) # Agrega el número dado a una lista. 
        matrizUno.append(listafilamatriz1) # Agrega la lista a la matriz principal. 
    
    for iterar in range(len(matrizUno)): # Recorre las filas de la matriz. 
        print(matrizUno[iterar]) # Imprime las filas. 

    return ("Matriz 1") # Duelve. 


def matrizTranspuestas (*args): # Definimos función. (Va a generar una matriz transpuesta. )
    
    matrizTranspuesta = [] # Generamos lista vacia. (Será la nueva matriz. )
    x = 0 # Establecemos variable. 
    for veces in range(columnaMatriz1): # Va a iterar tantas veces como columnas haya.
        lista = [] # Generamos lista vacia. (Se agregarán las sublistas)
        for n in range(filaMatriz1): # Va iterar tantas veces como filas haya. 
            valor = matrizUno[n][x] # Por cada iteración, tomara el indice de la lista de la iteración y la columna de la variable x. 
            lista.append(valor) # Agrega elemento a la lista. 
        x +=1 # Actualiza variable. 
        matrizTranspuesta.append(lista) # Agrega lista a la matriz. 

    for iterar in range(len(matrizTranspuesta)): # Itera las filas de la matriz. 
        print(matrizTranspuesta[iterar]) #Imprime las filas. 
    
    return ("Matriz transpuesta") # Devuelve. 


if __name__ == "__main__": # Permite inicializar la función. 
    filaMatriz1: int = int(input("Ingrese filas matriz 1: ")) # Pide valor.
    columnaMatriz1: int = int(input("Ingrese columnas matriz 1: ")) # Pide valor.
    print(crearMatrizUno(filaMatriz1, columnaMatriz1)) # Imprime función. 
    print(matrizTranspuestas(filaMatriz1, columnaMatriz1)) # Imprime función. 