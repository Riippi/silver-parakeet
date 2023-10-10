lista = ['Three', 'One', 'Maximuss', 'Howler', 'Naakka']

print(lista)


for nimi in lista:
    if len(nimi) > 5:
        print(len(nimi))

    if 'n' in nimi or 'N' in nimi:
        print("N")


while len(lista) > 0:
    lista.pop()


print(lista)
