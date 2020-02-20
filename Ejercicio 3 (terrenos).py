#Autor: Elena R.Tovar
#Calcular área de un terreno trapezoidal y determinar su costo
#Costo = $3450

bmayor = int(input ("Ingrese el valor de la base mayor en metros: "))
h = int (input ("Ingrese el valor de la altura en metros: "))
c = int (input ("Ingrese el valor en metros de diferencia del lado derecho menor con respecto a la base: " ))
d = int (input ("Ingrese el valor en metros de diferencia del lado izquierdo menor con respecto a la base: "))
bminor = float(bmayor-(c+d))
a = float(((bmayor+bminor)/2)*h)
p = float(a*3450)
print ("El precio del terreno es: $",p, "MXN")
