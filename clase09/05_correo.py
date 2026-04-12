correo = input("Ingrese un correo: ")
i=0
while i < len(correo):
    if correo[i]=='@':
        pos=i
    i=i+1

# Separar usuario y dominio
usuario = correo[0:pos]
dominio = correo[pos+1:]

print("Usuario:", usuario)
print("Dominio:", dominio)

# Clasificación según dominio
if dominio== "usm.cl":
    print("Correo institucional")
elif dominio == "gmail.com":
    print("Correo de Gmail")
else:
    print("Otro tipo de correo")
