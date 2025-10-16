def imposto(valor):
    valor_imposto = valor + (valor * 0.15)
    return valor_imposto

preco = float(input("Preço do produto: "))
print(f"Valor após impostos: R${imposto(preco):.2f}")