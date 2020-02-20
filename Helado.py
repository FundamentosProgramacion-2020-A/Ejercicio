# Autor: Fernando Pérez González
# Calcular área de una figura

r = int( input("Teclea el radio"))
h = int( input("Teclea la altura"))

a = (3.1416*r**2)/2 + (2*r*h)/2

print("Para un helado de radio y altura", r,h)
print("Área =", a)