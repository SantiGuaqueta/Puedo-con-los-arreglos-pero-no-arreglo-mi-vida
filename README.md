# Puedo-con-los-arreglos-pero-no-arreglo-mi-vida
El dia de hoy resolveremos los siguientes ejercicios propuesto en clase en este caso es el reto 10, pero antes... 
### Sabias que...

En la película, Bowser muestra un inesperado talento musical, algo que no estaba en el primer borrador del guion. Bowser canta una canción llamada Peaches, a la que Black le dio su toque personal

[![5-super-mario-bros-11-crop1680718468283-jpg-1036829263.webp](https://i.postimg.cc/wxsMPVpX/5-super-mario-bros-11-crop1680718468283-jpg-1036829263.webp)](https://postimg.cc/Z04Jv60n)


Ahora si, despues de este dato interesante estos son los ejercicios a resolver asi que manos a la obra:

1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
``` psudocode
# Ejercicio 1
n=int(input("Cantidad de datos en la lista: ")) #Pido cantidad de numeros que va a tener la lista
lista=[] # declaro una lista vacia que se utilizara mas adelante
suma=0 # suma se utilizara mas adelante para sumar los numeros de la lista
for x in range(0,n): 
    num=float(input("Escriba el numero: "))# Le pido un numero
    lista.append(num) # El numero que pedimos anterior se agregara a la lista 
    
for numero in lista:
    suma += numero # le pedimos que sume los numeros de la lista
Promedio= suma/len(lista) # Con los numeros sumados anteriormente los dividimos en la cantidad de digitos de la lista
print(Promedio) # Imprimimos el promedio
```

2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
``` psudocode
# Ejercicio 2
n=int(input("Cantidad de datos en la lista: ")) # Pido cantidad de numeros que va a tener la lista
lista=[] # declaro una lista vacia que se utilizara mas adelante
lista2=[]
for x in range(0,n):
    num=float(input("Escriba un numero para lista 1: "))# Le pido un numero
    lista.append(num) # El numero que pedimos anterior se agregara a la lista 

for x in range(0,n):
    num=float(input("Escriba un numero para lista 2: "))# Le pido un numero
    lista2.append(num) # El numero que pedimos anterior se agregara a la lista 

print("Su lista 1 es: " + str(lista))
print("Su lista 2 es: " +str(lista2))
producto_punto=0

for y in range(0,n):
    producto_punto += lista[y]*lista2[y]
print("El producto punto de las dos listas es: "+ str(producto_p

```
3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
``` pseudocode 
# Ejercicio 3
n=int(input("Cantidad de datos en la lista: ")) # Pido cantidad de numeros que va a tener la lista
lista=[] # declaro una lista vacia que se utilizara mas adelante
lista2=[]
for x in range(0,n):
    num=float(input("Escriba el numero: "))# Le pido un numero
    lista.append(num) # El numero que pedimos anterior se agregara a la lista 
    
for numero in lista: # Pido que la variable numero recorra la lista que antes se formo
    if numero == 0: # Le pido que si el numero es igual a 0 realice lo siguiente
        lista2.append(numero) # Lo que quiero que realize si cumpe la condicion del if es que lo agrege a la lista 2 que esta vacia
print(lista2)# Imprimo la lista 2 esta debe estar fuera del if y del for para que no se repita varias veces
```
