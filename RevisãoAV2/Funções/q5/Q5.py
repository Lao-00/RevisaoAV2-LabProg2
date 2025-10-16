def imc(peso, altura):
    calculo_imc = (peso / (altura**2))
    return calculo_imc

def classificar_imc(imc):
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 24.9:
        print("Peso normal")
    else: print("Acima do peso")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
print(imc(peso, altura))
print(classificar_imc(imc(peso, altura)))