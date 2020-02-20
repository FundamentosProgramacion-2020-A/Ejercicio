# Autor: Ani Martínez García
# Calcuar area, volumen y diametro de una esfera

r = int(input( "Ingrese radio=" ))
h = int(input("Ingrese altura ="))

areaSemicirculo = (1/2)*3.1416*r**2
areaTriangulo = (2*r)*h/2
areaTotal= areaSemicirculo + areaTriangulo


print ("areaSemicirculo", areaSemicirculo)
print ("areaTriangulo", areaTriangulo)
print ("areaTotal", areaTotal)





