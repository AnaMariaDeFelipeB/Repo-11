# Punto 1. 

def crearMatrizUno (*args):  # Definimos función. (Permite al usuario crear matrices)
    global matrizUno  # Definimos variable global. 
    matrizUno = [] # Creamos lista vacia. (Donde ingresaremos los valores de la matriz)
    for fila in range(matriz1): # Iteramos. (Vamos a generar la cantidad de filas)
        listafilamatriz1 = [] #Lista vacia. (Donde ingresaremos los valores de cada fila)
        for numero in range (matriz1): # Itera la longitud de la lista. 
            num : int = int(input("Ingrese número a la matriz número 1: ")) # Por cada iteración, va a preguntar un número. 
            listafilamatriz1.append(num) # Agrega el número dado a una lista. 
        matrizUno.append(listafilamatriz1) # Agrega la lista a la matriz principal. 
    
    for iterar in range(len(matrizUno)): # Recorre las filas de la matriz. 
        print(matrizUno[iterar]) # Imprime las filas. 

    return ("Matriz 1") # Duelve. 


def crearMatrizDos (*args): 
    global matrizDos 
    matrizDos = [] 
    for fila in range(matriz2): 
        listafilamatriz2 = [] 
        for numero in range (matriz2):  
            num : int = int(input("Ahora, ingrese número a la matriz número 2: "))
            listafilamatriz2.append(num)  
        matrizDos.append(listafilamatriz2) 
        
    for iterar in range(len(matrizDos)):  
        print(matrizDos[iterar]) 

    return ("Matriz 2") 


def sumaMatrices (*args):  # Definimos función. (Permite sumar matrices)
    
    matrizSuma = [] # Creamos lista vacia. (Donde agregaremos los valores de la matriz.)
    if matriz1 == matriz2: # Comprobamos si las matrices son iguales. 
        for i in range(len(matrizUno)): #Itera. (Va a generar la cantidad de filas)
            lista = [] # Creamos lista vacia. (Sera una subfila de la matriz)
            for j in range(len(matrizUno)): # Recorre cada elemento de la matriz. 
                suma = matrizUno[i][j] + matrizDos[i][j]  # Toma los valores de los indices de las filas y columnas y los suma. 
                lista.append(suma) # Agrega el valor a la subfila. 
            
            matrizSuma.append(lista) # Agrega la subfila a la matriz principal. 
        
        for iterar in range(len(matrizSuma)):  # Recorre las filas de la matriz. 
            print(matrizSuma[iterar]) # Imprime las filas. 

    else: # Si las matrices no son iguales, no desarrolla lo anterior. 
        print("Las matrices son de diferentes longitudes, volver a intentar.") # Imprime comentario. 
    
    return ("Matriz final (Suma)") # Devuelve. 


def restaMatrices (*args): 

    matrizResta = []

    if matriz1 == matriz2: 
        for i in range(len(matrizUno)):
            lista = []
            for j in range(len(matrizUno)): 
                resta = matrizUno[i][j] - matrizDos[i][j] # Toma los valores de los indices de las filas y columnas y los resta. 
                lista.append(resta)
            matrizResta.append(lista)
        
        for iterar in range(len(matrizResta)): 
            print(matrizResta[iterar])
    
    else: # Si las matrices no son iguales, no desarrolla lo anterior. 
        print("Las matrices son de diferentes longitudes, volver a intentar.") # Imprime comentario. 
    
    return ("Matriz final (Resta)") # Devuelve. 




if __name__ == "__main__": # Permite inicializar la función. 
    matriz1: int = int(input("Ingrese filas y columnas matriz 1: ")) # Pide valor.
    matriz2: int = int(input("Ingrese filas y columnas matriz 2: ")) # Pide valor.
    print(crearMatrizUno(matriz1)) # Imprime función. 
    print(crearMatrizDos(matriz2)) # Imprime función. 
    print(sumaMatrices(matriz1, matriz2)) # Imprime función. 
    print(restaMatrices(matriz1, matriz2)) # Imprime función. 