print("Benvenuto alla calcolatrice della differenza tra due orari")
print("ora inizio nel formato 'hh:mm' :")
inizio = input()
while (':' not in inizio):
    print("ATTENZIONE! ora inizio nel formato 'hh:mm' :")
    inizio = input()

print("ora del fine nel formato 'hh:mm' :")
fine = input()
while (':' not in fine):
    print("ATTENZIONE al formato! ora fine nel formato 'hh:mm' :")
    fine = input()

# from  datetime import datetime

# timeFormato = "%H:%M"

# timeDifferenza = datetime.strptime(fine, timeFormato) - datetime.strptime(inizio, timeFormato);
# print("La differenza tra i orari è: " + str(timeDifferenza));


array_inizio = inizio.split(':')

ora_inizio = int(array_inizio[0])


minuti_inizio = int(array_inizio[1])
if (minuti_inizio > 59):
    ora_inizio = ora_inizio + 1
    minuti_inizio = minuti_inizio - 60
    print(ora_inizio)
    print(minuti_inizio)

array_fine = fine.split(':')
ora_fine = int(array_fine[0])
ora_inizio = int(array_inizio[0])


minuti_fine = int(array_fine[1])
if (minuti_fine > 59):
    ora_fine = ora_fine + 1
    minuti_fine = minuti_fine - 60
    print(ora_fine)
    print(minuti_fine)

minuti_totale_inizio = ora_inizio * 60 + minuti_inizio

minuti_totale_fine = ora_fine * 60 + minuti_fine

if (minuti_totale_fine > minuti_totale_inizio):
    differenza = minuti_totale_fine - minuti_totale_inizio
    # print(differenza)
    ore_differenza = differenza // 60
    if (ore_differenza < 10):
        ore_differenza = "0" + str(ore_differenza)
    minuti_differenza = differenza % 60
    if (minuti_differenza < 10):
        minuti_differenza = "0" + str(minuti_differenza)
    differenza_format = str(ore_differenza) + ":" + str(minuti_differenza)
    print(differenza_format)

else:
    differenza = minuti_totale_inizio - minuti_totale_fine
    # print(differenza)
    ore_differenza = 24 - (differenza // 60)
    if (ore_differenza < 10):
        ore_differenza = "0" + str(ore_differenza)
    minuti_differenza = differenza % 60
    if (minuti_differenza < 10):
        minuti_differenza = "0" + str(minuti_differenza)
    differenza_format = str(ore_differenza) + ":" + str(minuti_differenza)
    print("Un giorno e " + differenza_format)






