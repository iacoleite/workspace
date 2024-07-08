import random

scelte_valide =["si","sisi","ok","okok" ,"certo" ,"andiamo" ,"va bene","ovvio","ovviamente","Y","y" ]
diversamente_valide = ["no","non so","non ancora"]

# In Python 0 è un valore falsy, cioè, ritorna False; 1 è True
testa= ["testa","Testa","TESTA","T","t",0,False]
croce= ["croce","Croce","CROCE","C","c",1,True]
valoreRisultato = 0;

print("Ciao cucc, benvenuto")

def ready():
  while True:
      readyness=input("Sei pronto?") 
      if readyness in scelte_valide :
          print ("Ottima scelta, iniziamo!!");
      elif readyness.isdigit ():
          print ("I numeri non valgono.")
          break;
      elif readyness in diversamente_valide:
          print  ("Immaginavo..riprova dopo");
          break;
      else:
          print("Non sono sicuro ma va bene..riprova dopo");
      return readyness

def scelta ():
  scelta=input ("Cosa scegli? 'Testa' o 'Croce' ? ")
  if scelta in testa:
   print("hai scelto testa");
  elif scelta in croce:
   print ("hai scelto croce") ;
  else:
    print('non ho capito, riprova.')
  return scelta

def risultato():
  valoreRisultato=random.randint(0,1);
  if valoreRisultato in testa:
   print ('e invece è testa.');
  elif valoreRisultato in croce: 
   print ('e invece è croce.');
  return valoreRisultato

def vittoria():
 vittoria=('hai vinto');
 if valoreRisultato in scelta:
#  while risultato==scelta:
   print (vittoria);
 else: 
   print ('dispiaceri..'); 
 return vittoria 

def retry():
 retry=input('Vuoi riprovare?')
 if retry in scelte_valide:
  #  print ('ok')(ready);
  print('OK');
 else :
   print ('ciao bè');
  
 return retry

def play():
  ready()
  scelta()
  risultato()
  vittoria()
  retry()

play(); 


#if ready in scelte_valide:
 #print ((scelta)+risultato)




      