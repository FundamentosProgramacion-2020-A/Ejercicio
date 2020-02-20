# Autor: Brandon Julien Celaya Torres
# Calcula figura helado

r = int( input("Teclea el radio: ") )
h = int( input("Teclea la altura: ") )

areaCirc = (3.1416*r**2)/2
areaTri = (2*r*h)/2
areaTotal= areaCirc+areaTri

print ("El área total es: ", areaTotal)

