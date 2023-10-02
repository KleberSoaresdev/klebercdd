while True:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if valor1 == valor2:
        print("Os valores são iguais. Por favor, insira valores diferentes.")
    else:
        break

if valor1 > valor2:
    valor1, valor2 = valor2, valor1

print(f"Valores em ordem crescente: {valor1}, {valor2}")