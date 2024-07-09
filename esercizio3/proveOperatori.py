# age = 15;

# if age >= 14:
#     print("Puoi prendere la patente per guidade il motorino");
#     if (age>=18):
#         print("Adesso sei maggiorenne");
#         print("Puoi nanche acquistare alcolici nei locali");
# else:
#     print("sei troppo piccolo! Non poui prendere il motorino.")


age = 18;
license = True;

if (age >= 18 and license == True):
    print("puoi noleggiare una ferrari!")
elif (age >= 18 and license == False):
    print("Fai prima la patente");
else:
    print("Ripassa tra qualche anno!");
          