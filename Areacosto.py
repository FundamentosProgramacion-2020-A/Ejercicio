# Autor: Maximiliano Garcia Tepale
# Actividad Area y costo

a1=int(input("leer valor de a:"))
b2=int(input("leer valor de b:"))
c3=int(input("leer valor de c:"))
d4=int(input("leer valor de d:"))

areat=d4*b2/2
areat1=(a1-c3-d4)*b2
areat2=c3*b2/2

at=areat+areat1+areat2

costo=at*3450

print(at,costo)