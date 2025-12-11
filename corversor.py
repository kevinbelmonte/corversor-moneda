print("===corversor de peso a dolar===")

pesos = float(input("ingresa el valor en pesos argentinos:"))

VALOR_DOLAR = 1000

dolares = pesos / VALOR_DOLAR

print(f"\nEquivalente aproximado en dolares: {dolares: .2f} USD")
