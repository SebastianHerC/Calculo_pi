import random 
import numpy



contador_d=0
contador_t=0


for i in range(0,10000):
    coordenada_x= random.random()
    coordenada_y=random.random()
    cond=(coordenada_x)**2 + (coordenada_y)**2
    contador_t+=1
    if cond<1:
        contador_d+=1 

pi=(contador_d*4)/(contador_t)
diferencia=abs((numpy.pi-pi))
porcentaje= ((diferencia*100)/numpy.pi)
print(pi)
print("_______________")
print(diferencia)
print("____________")
print(porcentaje)
