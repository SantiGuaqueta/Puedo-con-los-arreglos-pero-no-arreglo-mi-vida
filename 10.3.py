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
