t = int(input("Qual é a temperatura do momento? "))

frio = t < 25

print("Frio: ", frio)

if frio == False:
    print('Está calor.')
else:
    print('Está frio.')

print('Fim do programa.')
