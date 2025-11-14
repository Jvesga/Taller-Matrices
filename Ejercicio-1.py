#Leer una matriz de orden M*A y un numero K
#Multiplicar todos los elementos de la matriz por el numero K
#Mostrar la matriz resultante

matriz=[]
resultante=[]

K= int(input("Digite un numero entero: "))
M= int(input("Digite numero de filas: "))
A= int(input("Digite numero de columnas: "))
resultado=0

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

