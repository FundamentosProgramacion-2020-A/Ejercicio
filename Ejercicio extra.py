#Autor: Paloma Cueto
#Calcula el área de la figura

h= int(input ("Introduce el valor de la altura: "))
r= int(input ("Introduce el valor del radio: "))
triangulo = (r*2)*h/2
circulo = 3.1416*r**2/2

area = triangulo + circulo

print (" El área de la figura es: ", area )