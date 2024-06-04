menu= """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo =0
limite = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao =="d":
        valor = float(input("Informe o Valor do Depósito: "))

        if valor > 0:
            saldo == valor
            extrato == f"Depósito: R$ (valor: .2f)\n"

            else:
                print("Operação falhou! o valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))