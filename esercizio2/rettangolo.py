print("Benvenuto alla calculatrice della area e perimetro dello rettangolo!")
print("valore della base: ")
base = input();
print("valore della altezza: ")
altezza = input();

areaRettangolo = int(base) * int(altezza);
perimetroRettangolo = (int(base) * 2) + (int(altezza) * 2)

print("L'area del rettangolo è: " + str(areaRettangolo))
print("Il perimetro del rettangolo è: " + str(perimetroRettangolo))