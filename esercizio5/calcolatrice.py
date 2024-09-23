import math

def massimo(n, m, z = False):
    if (z == False):
        return n if (n >= m) else m
    else:
        return n if (n >= m and n >= z) else m if (m >= n and m >= z) else z if (z >= n and z >= m) else None

def minimo(n, m, z = False):
    if (z == "" or z == False):
        return n if (n <= m) else m
    else:
        return n if (n <= m and n <= z) else m if (m <= n and m <= z) else z if (z <= n and z <= m) else None

def somma(arr):
    return sum(arr)

def sottrazione(n, m):
    return float(n) - float(m)

def moltiplicazione(n, m):
    try:
        return float(n) * float(m)
    except ValueError:
        return "Inserire solamente numeri!"

def divisione(n, m):
    try:
        return float(n) / float(m)
    except ZeroDivisionError:
        return "impossibile dividere per 0"

def radiceQuadrata(base):
    return math.sqrt(float(base))

def potenza(n, m):
    return math.pow(float(n),float(m))

def massimoArray(arr):

    return max(arr)

def minimoArray(arr):
    return min(arr)

# def apreCalcolatrice():
#     print(splash)
#     while(True):
#         print(menu)
#         operazione = input("    Inserisci il numero corrispondente all'operazione da effettuare: ")
#         match operazione:
#             case "1":
#                 n = input("primo numero: ")
#                 m = input("secondo numero: ")
#                 print("Risultato: " + str(somma(n, m)))
#             case "2":
#                 n = input("primo numero: ")
#                 m = input("secondo numero: ")
#                 print("Risultato: " + str(sottrazione(n, m)))
#             case "3":
#                 n = input("primo numero: ")
#                 m = input("secondo numero: ")
#                 print("Risultato: " + str(moltiplicazione(n, m)))
#             case "4":
#                 n = input("primo numero: ")
#                 m = input("secondo numero: ")
#                 print("Risultato: " + str(divisione(n, m)))
#             case "5":
#                 base = input("base della radice: ")
#                 print("Risultato: " + str(radiceQuadrata(base)))
#             case "6":
#                 n = input("numero: ")
#                 m = input("potenza: ")
#                 print("Risultato: " + str(potenza(n, m)))
#             case "7":
#                 n = input("primo numero: ")
#                 m = input("secondo numero: ")
#                 z = input("terzo numero: ")
#                 print("Risultato: " + str(massimo(n, m, z)))
#             case "8":
#                 n = input("primo numero: ")
#                 m = input("secondo numero: ")
#                 z = input("terzo numero: ")
#                 print("Risultato: " + str(minimo(n, m, z)))
#             case "0":
#                 print("Ciao!")
#                 break
#             case default:
#                 print("Scelta invalida!")




