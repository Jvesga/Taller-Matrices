# Taller de matrices
# Nota:
Cada ejercicio tiene una breve explicacion del codigo usado al final.

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
## Explicacion del codigo.
primero se crean dos listas o arreglos vacios para almacenar la matriz original y otra para los resultados
despues se pide la constante identificada con (K), se pide el numero de filas de la matriz original identificada con la letra (M) y por ultimo se piden el numero de columnas con la variable (A).
despues se crea la matriz con la estructura for ya que en python se usa de esa forma
lo que hacen estas lineas es crear una estructura de matriz con vectroes siendo (M) las filas y A las columnas se crean vacias para almacenar despues datos.
despues se hace el llenado de la matriz pidiendo numeros al usuario y ubicandolos en cada posicion de la matriz con la linea de codigo 
```python
matriz[j][i]=int(input("Digite un numero: "))
```
posterior a eso se crea otra matriz vacia (M*A)
ahora se recorre cada fila y se multiplica cada elemento de la matriz original por la constante y se guarda en la matriz resultante.
y por ultimo se imprime el titulo y con un for se recorren las filas de la matriz resultante y se imprime cada elemento quitando el salto de linea con (end="")
y en la ultima linea se imprime un salto para mas estetica. 
