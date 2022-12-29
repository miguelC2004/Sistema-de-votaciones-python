
voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto5 = 0
voto = int(input('ingrese su voto o presione 0 para salir: '))
while voto != 0:
    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    elif voto == 4:
        voto4 += 1
    elif voto == 5:
        voto5 += 1

    voto = int(input('Su voto es para: '))

total_de_votos = voto1 + voto2 + voto3 + voto4 + voto5
candidatos = [voto1, voto2, voto3, voto4, voto5]
print("Total de votos " + str(total_de_votos))
contador = 0
for i in candidatos:
    contador += 1
    porcentaje = str(int((i/total_de_votos)*100)) + "%"
    print("El candidato " + str(contador) + " obtuvo " + str(i) + " votos, lo cual corresponden a un " + porcentaje + " del total de los votos.")
