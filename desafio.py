heroi = "isaias"
xp = 10.001

if xp <= 1.000:
    nível = "Ferro"
elif xp <= 1.001 and 2.000:
    nivel = "Bronze"
elif xp <= 2.001 and 5.000:
    nivel = "Prata"
elif xp <= 5.001 and 7.000:
    nivel = "Ouro"
elif xp <= 7.001 and 8.000:
    nivel = "Platina"
elif xp <= 8.001 and 9.000:
    nivel = "Ascendente"
elif xp <= 9.001 and 10.000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

print("O herói", heroi, "está no nível de", nivel)
