#Hacer un algoritmo que llene una matriz de 5 * 5 y 
#que almacene la diagonal principal en un vector. 
#Imprimir el vector resultante.

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
