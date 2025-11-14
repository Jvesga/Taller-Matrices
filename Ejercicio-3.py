# Hacer un algoritmo que llene una matriz de 3*3 y determine la posicion [Renglon, columna]
# del numero mayor almacenado en la matriz.

matriz = []

filas= 3
columnas= 3

for i in range (filas):
    matriz.append([])
    for j in range(columnas):
        matriz[i].append(None)

for j in range (0,filas):
    for i in range(0,columnas):
        matriz[j][i]=int(input("Digite un numero: "))
    
print("\nMatriz resultante:")
for M in matriz:
    for elemento in M:
        print(f"{elemento}", end=" ")
    print()

numero_M = matriz[0][0]
filaM=0
columnaM=0

for i in range(3):
    for j in range(3):
        if matriz [i][j] > numero_M:
            numero_M=matriz[i][j]
            filaM=i+1
            columnaM=j+1
print(f"El numero mayo se encuentra en: la fila {filaM} y la columna {columnaM} y es el numero {numero_M}")
