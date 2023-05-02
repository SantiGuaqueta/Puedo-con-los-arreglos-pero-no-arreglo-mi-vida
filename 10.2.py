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
print("El producto punto de las dos listas es: "+ str(producto_punto))