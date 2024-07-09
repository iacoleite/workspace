counter = 0;

while counter <= 10:
    print(counter)
    counter += 1;



righe = 0;
altezza = 10;

posizione_cursor = 0;
while posizione_cursor <= altezza:
    print("A" * posizione_cursor)
    posizione_cursor += 1
print();


counter = 0;
run = True
stop = 15
skip=3

# while run == True:
#    print(counter)
#    counter += 1
#    if counter > stop:
#        print("sto uscendo dal loop...")
#        break

while counter < 10:
    counter += 1
    if counter == skip:
        print(f"sto saltando {skip}")
        continue
    # continue fa tornare allo inizio del ciclo
    print(counter)
