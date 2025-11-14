#Hacer un algoritmo que llene una matriz de 4*4. 
#Calcular la suma de cada renglón y almacenarla en un vector, 
#la suma de cada columna y almacenarla en otro vector.

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
