### <div align="center"> **Control Taller de Programación Sección 3**
</div>

**Nombre:** ............................................................................................................................................................


Resuelva individualmente los siguientes problemas. Puede apoyarse en material escrito o impreso pero **NO** en material digital o Internet.


**1- Sumatoria de una serie geométrica [1.0 pt]**: Escriba un programa en Python que solicite al usuario un número entero positivo \(n\) y calcule e imprima en pantalla el resultado de la sumatoria de la serie geométrica desde \(k=0\) hasta \(n\), según la siguiente fórmula:

$S = \sum_{k=0}^{n} \frac{1}{(2k+1)^k}$

```python
#Alternativa 1
n=int(input('Ingrese un entero positivo'))
suma=0
for k in range(0, n+1):
	suma+=1/(2*k+1)**k
print(suma)
```


```python
#Alternativa 2
n=int(input('Ingrese un entero positivo'))
suma=0
k=0

while k<=n:
	suma+=1/(2**k+1)**k
	k+=1
print(suma)
```



**2- Interseccion de listas [2.0 pts]**: A partir de las listas L1 y L2,  calcule la intersección de ellas sin usar sets.

```python
L1 = [1,2,10,4,7, 21,8,3]
L2 = [2,7,1,21,6,9]
```

```python
#Alternativa 1
interseccion=[]
for numero in L1:
	if numero in L2:
		interseccion.append(numero)
		
print(interseccion)
```

```python
#Alternativa 2
interseccion=[]
for numero in L2:
	if numero in L1:
		interseccion.append(numero)
		
print(interseccion)
```

**3- Verificación de contraseña [2.0 pts].** Escriba un programa que solicite la creación de una contraseña para un sitio web y verifique que cumple tres reglas mínimas: debe tener un largo minimo de 8 carácteres, debe contener al menos un dígito y debe contener al menos uno de los siguientes caracteres especiales: `'*'`, `'#'`, `'-'`, `'$'`.

Si la contraseña cumple con todas las reglas debe imprimir en pantallla **'Contraseña valida'**, de lo contrario debe imprimir **'Contraseña invalida**'.

```python
contraseña=input('Ingrese contraseña:')

digitos=[0,1,2,3,4,5,6,7,8,9]
caracteres=['*', '#', '-', '$']

verificador1=False
verificador2=False

for letra in contraseña:
	if letra in digitos:
		verificador1=True
		break

for letra in contraseña:
	if letra in caracteres:
		verificador2=True
		break
		
if len(contraseña) >=8 and verificador1==True and verificador2==True:
	print('Contraseña valida')
else:
	print('Contraseña invalida')
	

```


**4- Evaluar salida [2.0 pts].**Escriba la salida de este código (valor final de la variable A). Fundamente.

```python
N = int(input("Ingrese un número entero positivo"))
A = [False] * N
i = 0
while i * i <= N:
    A[i * i] = True
    i += 1
print(A)
```

Para N=10

| Iteración | `i`  | `A`                                      |
|-----------|------|------------------------------------------|
| 1         | 0    | [**True**, False, False, False, False, False, False, False, False, False] |
| 2         | 1    | [True, **True**, False, False, False, False, False, False, False, False] |
| 3         | 2    | [True, True, False, False, **True**, False, False, False, False, False] |
| 4         | 3    | [True, True, False, False, True, False, False, False, False, False]    |








