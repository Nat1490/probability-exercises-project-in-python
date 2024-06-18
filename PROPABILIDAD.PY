# TODO
import random

def Tdados():
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    
    suma= d1+d2
    return suma
cont=0
for _ in range (1000):
    suma = Tdados()
    if suma >7 or suma %2:
        cont+=1
probabilidad=cont/1000
print(f"La probabilidad de que la suma de los dados sea mayor que 7 o un número par es: {probabilidad}")