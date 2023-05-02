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