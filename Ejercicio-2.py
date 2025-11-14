#Lea dos matrices N * M y a continuación:

#a)Genere una tercera con la suma de ambas
#b)Genere una cuarta con la multiplicación de ambas, si es posible
#Muestre las matrices resultantes


filas_A = int(input("Filas de matriz A: "))
columnas_A = int(input("Columnas de matriz A: "))

filas_B = int(input("Filas de matriz B: ")) 
columnas_B = int(input("Columnas de matriz B: ")) 

matriz_A = []
for i in range(filas_A):
    matriz_A.append([])
    for j in range(columnas_A):
        matriz_A[i].append(None)

for i in range(filas_A):
    for j in range(columnas_A):
        matriz_A[i][j] = int(input(f"inserte el numero de la posicion [{i+1}][{j+1}]de la matriz A: "))

matriz_B = []
for i in range(filas_B):
    matriz_B.append([])
    for j in range(columnas_B):
        matriz_B[i].append(None)


for i in range(filas_B):
    for j in range(columnas_B):
        matriz_B[i][j] = int(input(f"inserte el numero de la posicion [{i+1}][{j+1}] de la matriz B: "))


print("Matriz A:")
for i in range(filas_A):
    for j in range(columnas_A):
        print(matriz_A[i][j], end=" ")
    print()


print("Matriz B:")
for i in range(filas_B):
    for j in range(columnas_B):
        print(matriz_B[i][j], end=" ")
    print()


if filas_A == filas_B and columnas_A == columnas_B:
    matriz_C = []
    for i in range(filas_A):
        fila = []
        for j in range(columnas_A):
            suma = matriz_A[i][j] + matriz_B[i][j]
            fila.append(suma)
        matriz_C.append(fila)
    
    print("Matriz C:")
    for i in range(filas_A):
        for j in range(columnas_A):
            print(matriz_C[i][j], end=" ")
        print()

if columnas_A == filas_B:
    matriz_D = []
    for i in range(filas_A):
        fila = []
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma = suma + matriz_A[i][k] * matriz_B[k][j]
            fila.append(suma)
        matriz_D.append(fila)
    
    print("Matriz D:")
    for i in range(filas_A):
        for j in range(columnas_B):
            print(matriz_D[i][j], end=" ")
        print()