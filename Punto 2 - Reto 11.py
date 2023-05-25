# Punto 2. 

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


def crearMatrizDos (*args): 
    global matrizDos 
    matrizDos = [] 
    for fila in range(filaMatriz2): 
        listafilamatriz2 = [] 
        for numero in range (columnaMatriz2):  
            num : int = int(input("Ahora, ingrese número a la matriz número 2: "))
            listafilamatriz2.append(num)  
            
        matrizDos.append(listafilamatriz2) 
        
    for iterar in range(len(matrizDos)):  
        print(matrizDos[iterar]) 

    return ("Matriz 2") 

def multiplicarMatrices (*args): # Definimos la función. (Permite multiplicar matrices)

    matrizMultiplicada =[] # Creamos lista vacia. (Donde ingresaremos los valores de la matriz)
    if columnaMatriz1 == filaMatriz2: # Definimos condición. (Que la columna de la matriz 1 sea igual a la fila de matriz 2. Para poder operar las matrices.)
        for fila in range(filaMatriz1): # Itera tantas veces como filas dde la matriz 1 haya. 
            lista = [] # Lista vacia. (Sublista de la matriz) 
            x : int = 0 # Variable. (La iremos actualizando)
            while x < columnaMatriz2: # Establecemos un ciclo. (Impide que una vez itere lo de abajo avance, sino que continua para poder multiplicar cada columna)
                operacion : int = 0 # Definimos variable. (Actualiza y limpia la operación)
                for columna in range(filaMatriz2): # Itera tantas veces como filas de la matriz 2 haya.
                    producto = (matrizUno[fila][columna])*(matrizDos[columna][x]) # Multiplica la matriz 1 por la matriz 2. 
                    operacion = operacion + producto # Actualiza. 
                x +=1 # Actualiza. (Para que el ciclo no sea infinito)
                lista.append(operacion) # Agrega la operación a la lista. 
            matrizMultiplicada.append(lista) # Agrega la lista a la matriz. 
    else: # Si la matriz no se puede multiplicar, porque no cumple las condiciones, continua e imprime lo de abajo. 
        print("No se puede operar la matriz, debido a que no continene filas y columnas iguales, intentar nuevamente")   

    for iterar in range(len(matrizMultiplicada)): # Recorre las filas de la matriz. 
        print(matrizMultiplicada[iterar]) # Imprime las filas. 


    return ("Matriz multiplicada") # Devuelve. 


    
if __name__ == "__main__": # Permite inicializar la función. 
    filaMatriz1: int = int(input("Ingrese filas matriz 1: ")) # Pide valor.
    columnaMatriz1: int = int(input("Ingrese columnas matriz 1: ")) # Pide valor.
    filaMatriz2: int = int(input("Ingrese filas matriz 2: ")) # Pide valor.
    columnaMatriz2: int = int(input("Ingrese columnas matriz 2: ")) # Pide valor.
    print(crearMatrizUno(filaMatriz1, columnaMatriz1)) # Imprime función. 
    print(crearMatrizDos(filaMatriz2, columnaMatriz2)) # Imprime función. 
    print(multiplicarMatrices(filaMatriz1, columnaMatriz1, filaMatriz2, columnaMatriz2))

#Pd. Casi que no lo logro. Otro reto sufrido