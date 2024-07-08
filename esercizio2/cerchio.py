import math

# print(math.pi)

print("Benvenuto alla calculatrice dell'area del cerchio!")
print("Valore del raggio:")
raggio = input()

areaCerchio = math.pi * float(raggio)**2;

print("L'area del cerchio è " + str(areaCerchio))
