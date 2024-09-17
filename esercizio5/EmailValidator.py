def validaMail(email):
    contemArroba = email.__contains__("@")
    split1 = str(email).split("@")
    split2 = str(split1[1]).split(".")

    if contemArroba == True and email.endswith("@") == False and email.startswith("@") == False and email.count("@") == 1 and (
            2 <= len(split2[1]) < 4):
        return True
    else:
        return False


def validaCap(codice):
    if len(codice) != 5:
        return False
    elif (not codice.isnumeric()):
        return False
    else:
        return True


def validaTelefono(telefono):
    telefono = str(telefono).replace(" ", "")
    # print(telefono[1:])
    numerico = telefono[1:].isnumeric()
    # print(numerico)
    if str(telefono).startswith("+") and numerico == True and len(telefono) == 13:
        return True
    else:
        return False




