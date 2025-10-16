def desconto(valor):
    novo_valor = valor - (valor * 0.1)
    return novo_valor

preco = float(input("Insira o preço do produto: "))
print(f"Valor após desconto: R${desconto(preco):.2f}")