import random;


x = 3;
y = 5;

risultato = x + y;
print(risultato);

print('python è una merda di linguaggio per la dinamicita dei tipi')
x = 2;
print(type(x));
x = 2 / 2;
print(type(x));

stringa = "ciao";

print(type(stringa));
# print(stringa[0]);

print();

def printOgniLinea(strAlvo): 
    for i in range (len(strAlvo)):
        print(strAlvo[i].upper());
printOgniLinea(stringa);

def mezzoArbelo():
    for y in range (10):
        print(y * '*');

mezzoArbelo();

print();
citazione = "L'autore scrisse:  \"Nel bel mezzo del cammin\"";
print(citazione);
print();

stringa1 = "veni, vidi, ";
stringa2 = "vici";
stringa3 = stringa1 + stringa2;
print(stringa3);

# printOgniLinea(stringa3);


age = 37;
text = "La mia età è: "

messagio = text + str(age);
print(messagio);

# eta = input("Quanti anni hai? ");
# textALei = "La tua età è: "
# messagio = textALei + str(eta);
# print(messagio);

numeroAleatorio = random.randint(0, 50);
print(numeroAleatorio);

numeroProva = -1;
while (x != numeroAleatorio):
    numeroProva = input("Sceglie un numero: ");
    # print(numeroProva);
    if (int(numeroProva) < numeroAleatorio):
        print("numero segreto è maggiore che " + numeroProva + "!");
    if (int(numeroProva) > numeroAleatorio):
        print("numero segreto è minori che " + numeroProva + "!");  
    if (int(numeroProva) == numeroAleatorio):
        print("HAI VINTO!!!");
        break;
print("BRAVO!");

numeriDiLanci = input("Quanti volte vuoi lanciare la moneta? ")

for i in range(int(numeriDiLanci)):
    valoreMoneta = random.randint(0, 1);
    if (valoreMoneta == 0):
        # print(valoreMoneta);
        print("testa");
    else:
        print("croce");
        # print(valoreMoneta);






