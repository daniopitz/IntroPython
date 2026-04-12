from random import randint
a=True 
while a==True:
    numero=randint(1,6)
    if numero ==6:
        print('Salio el numero 6')
        a=False
    else:
        print('Intenta otra vez')
