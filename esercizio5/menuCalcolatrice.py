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

        0. Uscire
"""
def apreCalcolatrice():
    print(splash)
    while(True):
        print(menu)
        operazione = input("    Inserisci il numero corrispondente all'operazione da effettuare: ")
        match operazione:
            case "1":
                n = input("primo numero: ")
                m = input("secondo numero: ")
                print("Risultato: " + str(calcolatrice.somma(n, m)))
            case "2":
                n = input("primo numero: ")
                m = input("secondo numero: ")
                print("Risultato: " + str(calcolatrice.sottrazione(n, m)))
            case "3":
                n = input("primo numero: ")
                m = input("secondo numero: ")
                print("Risultato: " + str(calcolatrice.moltiplicazione(n, m)))
            case "4":
                n = input("primo numero: ")
                m = input("secondo numero: ")
                print("Risultato: " + str(calcolatrice.divisione(n, m)))
            case "5":
                base = input("base della radice: ")
                print("Risultato: " + str(calcolatrice.radiceQuadrata(base)))
            case "6":
                n = input("numero: ")
                m = input("potenza: ")
                print("Risultato: " + str(calcolatrice.potenza(n, m)))
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
            case "0":
                print("Ciao!")
                quit()
            case default:
                print("Scelta invalida!")


            # if operazine == "1":
            #     n = input("primo numero: ")
            #     m = input("secondo numero: ")
            #     print("Risultato: " + str(calcolatrice.somma(n, m)))
            # elif operazione == "2":
            #     n = input("primo numero: ")
            #     m = input("secondo numero: ")
            #     print("Risultato: " + str(calcolatrice.somma(n, m)))
            #     ...

