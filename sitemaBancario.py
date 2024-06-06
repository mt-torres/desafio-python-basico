menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
->"""
saldo = 0
limite = 500
extrato = []
LIMITE_SAQUES = 3
contarRetiradasDiarias = 0;

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato.append({"Deposito": valor})
            print("Valor depositado com sucesso!")
        else:
            print("Não foi possível realizar essa transação. por favor verifique o valor e tente novamente.")

    elif opcao == "s":
        valor = float(input("Informe o valor a ser retirado: "))
        if contarRetiradasDiarias == LIMITE_SAQUES:
            print(f"Não foi possível realizar essa transação. O limite de {LIMITE_SAQUES} saques diários foi atingido. Tente novamente amanhã.")
        elif saldo == 0:
            print("Não foi possível realizar essa transação. A conta não possui saldo para retirada.")
        elif valor <= saldo and valor <= limite:
            saldo -= valor
            contarRetiradasDiarias += 1
            extrato.append({"Saque": valor})
            print("Valor retirado com sucesso!")
        else:
            print("Não foi possível realizar essa transação. por favor verifique o valor e tente novamente.")

    elif opcao == "e":
        print("===================== Extrato =====================")
        for movimento in extrato:
            for chave, valor in movimento.items():
                print(f"Tipo operação: {chave} - valor: R$ {valor:.2f}")
                
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================================")



    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços, volte sempre!")
        break

    else:
        print("Opção inválida, por favor seleciona uma das opções e tente novamente")

