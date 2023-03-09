t = int(input("Qual é a temperatura? "))

if t < 10:
    print("Está frio.")
elif t >= 10 and t <= 30:
    print("Está agradável.")
else: 
    print("Está calor.")
