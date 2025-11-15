# Taller de matrices

## Ejercicio 1.
Leer una matriz de orden M*A y un numero K
Multiplicar todos los elementos de la matriz por el numero K
Mostrar la matriz resultante

``` python
matriz=[]
resultante=[]

K= int(input("Digite un numero entero: "))
M= int(input("Digite numero de filas: "))
A= int(input("Digite numero de columnas: "))

for i in range (M):
    matriz.append([])
    for j in range(A):
        matriz[i].append(None)

for j in range (0,M):
    for i in range(0,A):
        matriz[j][i]=int(input("Digite un numero: "))
        multipricar = matriz[j][i] * K



for a in range (M):
    resultante.append([])
    for b in range(A):
        resultante[a].append(None)

for c in range(0,M):
    for d in range(0,A):
        resultante[c][d]=int(multipricar)


print("\nMatriz resultante:")
for M in resultante:
    for elemento in M:
        print(f"{elemento}", end=" ")
    print()
```
## Ejercicio 2.
Lea dos matrices N * M y a continuación:
a)Genere una tercera con la suma de ambas
b)Genere una cuarta con la multiplicación de ambas, si es posible
Muestre las matrices resultantes

``` python
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
```
## Ejercicio 3.
Hacer un algoritmo que llene una matriz de 3*3 y determine la posicion [Renglon, columna]
del numero mayor almacenado en la matriz.

``` python
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
```
## Ejercicio 4.
Hacer un algoritmo que llene una matriz de 4*4. 
Calcular la suma de cada renglón y almacenarla en un vector, 
la suma de cada columna y almacenarla en otro vector.

``` python
matriz=[]


for i in range (4):
    matriz.append([])
    for j in range(4):
        matriz[i].append(None)

for j in range (0,4):
    for i in range(0,4):
        matriz[j][i]=int(input("Digite un numero: "))

print("---Suma de renglones---")
suma_renglones=[]
for i in range(4):
    suma=0
    for j in range(4):
        suma=suma + matriz[i][j]
    suma_renglones.append(suma)
print(suma_renglones)

print("---Suma de columnas---")
suma_columnas=[]
for j in range(4):
    suma2=0
    for i in range(4):
        suma2= suma2 + matriz[i][j]
    suma_columnas.append(suma2)
print(suma_columnas)
```
## Ejercicio 5.
Hacer un algoritmo que llene una matriz de 5 * 5 y 
que almacene la diagonal principal en un vector. 
Imprimir el vector resultante.

``` python
matriz = []

filas= 5
columnas= 5

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

diagonal=[]

for i in range(5):
    numero = matriz[i][i]
    diagonal.append(numero)
    print(f"Posicion [{i+1}][{i+1}] = {numero}")
print("---Diagonal de la matriz 5*5---")
print(diagonal)
```
