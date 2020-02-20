#Autor: Sharone Márquez
#Calcular  area de la figura

h= int(input("Introducir el valor de la altura: "))
r= int(input("Introducir el valor del radio: "))
triangulo = (r*2)*h/2
circulo= 3.1416*r**2/2
Area= triangulo + circulo
print("El area es: ", Area)