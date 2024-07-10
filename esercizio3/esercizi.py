"""
1- Prendere in input 2 numeri e fornire in output il valore massimo

2- Prendere in input 3 numeri e fornire in outuput il valore minimo tra i 3

3-  dall'esercizio 3 della scorsa volta verificar con il ciclo while che fli input siano numeri vallidi

4- la prima volta che l'uomo è andato sulla luna è stato il 1969 creare un programa che chiede l'anno di nascita all'utente
    e risponde se è nato l'anno in cui l'uomo è andato sulla luna e quanti anni prima o quanti anni dopo

5- il programma legge tre numero li mette in ordine crescente

6- simulare un'asta in cui ci siano due compratori che si contendono l'acquisto di un oggetto,
     a turno i due compratori dovranno fare un'offerta per l'oggeto da comprare, 
     l'asta termina quando uno dei due compratori si ritira offrendo '0', a quel punto l'0altro compratore si saròa aggiudicato al'asta.
    Stampare quale compratore si è aggiudicato l'asta e con che cifra

"""
# ESERCIZIO 1
# numero_1 = input("Uno numero: ")
# numero_2 = input("Altro numero: ")

# if (numero_1 > numero_2):
#     print(f"il numero massimo è {numero_1}")
# else:
#     print(f"il numero massimo è {numero_2}")



# ESERCIZIO 2 e 3

# print("sceglie 3 numeri: ")

# a = input("numero 1: ");
# while (a.isnumeric() != True):
#     print("Deve sceglie un numero")
#     a = input("numero 1: ");

# b = input("numero 2: ");
# while (b.isnumeric() != True):
#     print("Deve sceglie un numero")
#     b = input("numero 2: ");

# c = input("numero 3: ");
# while (c.isnumeric() == False):
#     print("Deve sceglie un numero")
#     c = input("numero 1: ");

# numero_minimo =a
# if (b < numero_minimo ):
#     numero_minimo=b
# if (c < numero_minimo):
#     numero_minimo = c

# print(f"il numero minimo è {numero_minimo}")




# ESERCIZIO 4
# print()
# anno_di_nascita = input("Quando sei natto? ");
# if (int(anno_di_nascita) == 1969):
#     print("Sei natto nello stesso anno che l'uomo è arrivato sulla luna!")
# elif (int(anno_di_nascita) < 1969):
#     anni_prima = 1969 - int(anno_di_nascita);
#     print(f"Sei natto {anni_prima} anni prima che l'uomo è arrivato sulla luna!")
# else:
#     anni_dopo = int(anno_di_nascita) - 1969;
#     print(f"Sei natto {anni_dopo} anni dopo che l'uomo è arrivato sulla luna!")



# ESERCIZIO 5
print("sceglie 3 numeri: ")

a = input("numero 1: ");
b = input("numero 2: ");
c = input("numero 3: ");

a = int(a)
b = int(b)
c = int(c)

# lista = []
# lista.append(a)
# lista.append(b)
# lista.append(c)
# lista.sort();
# print(lista)

if (b < a):
    a, b = b, a
if (c < b):
    b, c = c, b
if (b < a):
    a, b = b, a

print(f"In ordine crescente: {a}, {b}, {c}")

# # ESERCIZIO 6

# print("Benvenuto all'asta della ferrari che come sei minorenne non puoi guidare!")
# print("per retirarsi deve fare una offerta di valore 0")

# usuario1 = input("Usuario 1, faccia una offerta: ")
# usuario2 = input("Usuario 2, faccia una offerta: ")
# valore_piu_alto = 0;
# if (int(usuario1) > valore_piu_alto):
#     valore_piu_alto = int(usuario1)
# if (int(usuario2) > valore_piu_alto):
#     valore_piu_alto = int(usuario2)

# while (usuario1 != "0" and usuario2 != "0"):
#     print(f"Valore attuale: {valore_piu_alto}")
#     usuario1 = input("Usuario 1, faccia una offerta: ")
#     if (int(usuario1) > valore_piu_alto):
#         valore_piu_alto = int(usuario1)
#     usuario2 = input("Usuario 2, faccia una offerta: ")
#     if (int(usuario2) > valore_piu_alto):
#         valore_piu_alto = int(usuario2)





