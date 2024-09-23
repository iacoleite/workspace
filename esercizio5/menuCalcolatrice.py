from os import system

import calcolatrice

splash = """
            _           _       _        _          
           | |         | |     | |      (_)         
   ___ __ _| | ___ ___ | | __ _| |_ _ __ _  ___ ___ 
  / __/ _` | |/ __/ _ \| |/ _` | __| '__| |/ __/ _ \\
 | (_| (_| | | (_| (_) | | (_| | |_| |  | | (_|  __/
  \___\__,_|_|\___\___/|_|\__,_|\__|_|  |_|\___\___|
   """

menu = """    Menu di Operazione
        1. +
        2. -
        3. x
        4. /
        5. Radice quadrata
        6. Esponenziale
        7. Numero massimo tra 2 o 3 numeri
        8. Numero minimo tra 2 o 3 numeri
        9. Numero massimo tra X numeri
       10. Numero minimo tra X numeri

        0. Uscire
"""




def apreCalcolatrice():

    print(splash)
    while(True):
        print(menu)
        operazione = input("    Inserisci il numero corrispondente all'operazione da effettuare: ")
        match operazione:
            case "1":
                arr = prende2numeri()
                print("Risultato: " + str(calcolatrice.somma(arr)))
            case "2":
                arr = prende2numeri()
                print("Risultato: " + str(calcolatrice.sottrazione(arr[0], arr[1])))
            case "3":
                arr = prende2numeri()
                print("Risultato: " + str(calcolatrice.moltiplicazione(arr[0], arr[1])))
            case "4":
                arr = prende2numeri()
                print("Risultato: " + str(calcolatrice.divisione(arr[0], arr[1])))
            case "5":
                base = input("base della radice: ")
                print("Risultato: " + str(calcolatrice.radiceQuadrata(base)))
            case "6":
                arr = prende2numeri()
                print("Risultato: " + str(calcolatrice.potenza(arr[0], arr[1])))
            case "7":
                n = input("primo numero: ")
                m = input("secondo numero: ")
                z = input("terzo numero (opzionale): ")
                print("Risultato: " + str(calcolatrice.massimo(n, m, z)))
            case "8":
                n = input("primo numero: ")
                m = input("secondo numero: ")
                z = input("terzo numero (opzionale): ")
                print("Risultato: " + str(calcolatrice.minimo(n, m, z)))
            case "9":
                n = input("Quanti numeri vuole inserire? ")
                a = prendeXnumeri(int(n))
                print("Il numero massimo è: " + calcolatrice.massimoArray(a))
            case "10":
                n = input("Quanti numeri vuole inserire? ")
                arr = prendeXnumeri(int(n))
                print("Risultato: " + calcolatrice.minimoArray(arr))
            case "0":
                print("Ciao!")
                quit()
            case default:
                print("Scelta invalida!")

def prende2numeri():
    n = input("primo numero: ")
    m = input("secondo numero: ")
    try: 
        return [float(n), float(m)]
    except ValueError:
        return "Solamente numeri!"

def prendeXnumeri(n):
    arr = []
    for i in range (n):
        numero = input(f"Inserisci il {i+1} elemento: ")
        arr.append(int(numero))
    return arr

