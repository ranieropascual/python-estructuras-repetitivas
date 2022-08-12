print("-----------------------------------------------------------------")
print("ejercicio2 calcula el interes")
print("-----------------------------------------------------------------")
#inicializacion
C=-1
I=0
M=0
#entradas
while (C<0)or(I<=0)or (I>=100)or(M<=0):
    print("introduce el capital, el interes y el tiempo apropiados")
    C=int(input("capital: "))
    I=int(input("interes: "))
    M=int(input("tiempo en años: "))
#procesos
for I in range(M):
    C=C*(1+I/100)
#salida
print("tienes $",C,"dolares")

