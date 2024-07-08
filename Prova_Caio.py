import random

scelte_valide =["si","sisi","ok","okok" ,"certo" ,"andiamo" ,"va bene","ovvio","ovviamente","Y","y" ]
diversamente_valide = ["no","non so","non ancora"]

# In Python 0 è un valore falsy, cioè, ritorna False; 1 è True
testa= ["testa","Testa","TESTA","T","t",0,False]
croce= ["croce","Croce","CROCE","C","c",1,True]

continuatore = 1

def play():
    scelta=input ("Cosa scegli? 'Testa' o 'Croce' ? ")
    
    if scelta in testa:
        print("hai scelto testa");
    elif scelta in croce:
        print ("hai scelto croce");
    else:
        print('non ho capito, riprova.')
    valoreRisultato = getRisultatoLancio();
#   print(valoreRisultato)

    if (valoreRisultato in testa):
        print(valoreRisultato)
        print(scelta)
        print("hai vinto!")
    elif (valoreRisultato in croce):
        print(valoreRisultato)
        print(scelta)
        print("hai vinto!")
    else:
        print(valoreRisultato)
        print(scelta)
        print("hai vinto!")




def getRisultatoLancio():
    valoreRisultato=random.randint(0,1);
    return valoreRisultato;


while (continuatore != 0):
    
    readyness = "si";
    readyness=input("Sei pronto?")

    if (readyness in scelte_valide):
        print ("Ottima scelta, iniziamo!!");
        play();
    elif readyness.isdigit():
        print("I numeri non valgono.")
        continuatore = 0;
    elif readyness in diversamente_valide:
        print("Immaginavo..riprova dopo");
        continuatore = 0;
    else:
        print("Non sono sicuro ma va bene..riprova dopo");


    

    

