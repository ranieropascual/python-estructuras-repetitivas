print("-----------------------------------------------------------")
print("ejercicio2 calcula la suma de los divisores")
print("-----------------------------------------------------------")

#entradas
print("introduce un numero, y para acabar uno negativo")
numero = int(input("num: "))
while numero > 0:
    suma = 0

    for i in range(1,numero+1):
        if numero % i ==0:
            suma = suma + i
#salida
print("------------------------------------------------------------")            
print("la suma de los divisores del numero es: ", suma, "/n")

print("introduce un numero, y un numero negativo para acabar")
numero=int(input("num: "))