def maior(idade):
    if idade >= 18:
        print("Maior de idade")
    else: print("Menor de idade")

idade = int(input("Insira sua idade: "))
print(maior(idade))