import EmailValidator

x = input("Inserisci il tuo e-mail: ")
valido = EmailValidator.validaMail(x)
while (valido == False):
    x = input("E-mail non è valido. Inserisci un e-mail valido: ")
    valido = EmailValidator.validaMail(x)

y = input("Inserisci il tuo telefono con prefisso internazionale: ")
validaTel = EmailValidator.validaTelefono(y)
while (validaTel == False):
    y = input("Telefono non è valido. Inserisci un numero valido: ")
    valido = EmailValidator.validaTelefono(y)


z = input("Inserisci il tuo cap: ")
capValido = EmailValidator.validaCap(z)
while (capValido == False):
    z = input("Inserisci il tuo cap: ")
    capValido = EmailValidator.validaCap(z)

print(f"Email: {x}")
print(f"Telefono: {y}")
print(f"CAP: {z}")

