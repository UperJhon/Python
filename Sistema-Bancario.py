saldo = 0
numero_saque = 0
LIMITE_SAQUE = 3
limite_por_saque = 500
extrato = ""


print("OLÁ! SEJA BEM VINDO.")

while True:

    operacao = int(input("""
                           
1 - Depósito
2 - Saque
3 - Extrato
4 - Sair                
                                  
>>> """))

    if operacao == 1:
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"

        else:
            print("Operacao inválida. Informe o valor novamente.")

    elif operacao == 2:

        valor = float(input("Informe o valor do saque: R$"))

        excede_saldo = valor > saldo

        excede_limite = valor > limite_por_saque

        excede_saque = numero_saque >= LIMITE_SAQUE

        if excede_saldo:
            print("Saldo insuficiente.")

        elif excede_limite:
            print("O valor excede o limite por saque de R$ 500,00.")

        elif excede_saque:
            print("""
                  
                  Poxa vida. O seu limite de operações dárias para saque ainda é de 3. Identificamos que o Sr(a). já realizou outras operações. 
                  Por isso pedimos que realize uma nova operação.")

                  """)

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Valor inválido. Informe-o novamente.")

    elif operacao == 3:
        print("\n================= EXTRATO =================\n")
        print("Nenhuma operação foi realizada até o momento.\n" if not extrato else extrato)
        print("===========================================")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("===========================================")

    elif operacao == 4:
        print("Obrigado pela preferência. Ficamos à disposição.")
        break

    else:
        print("Operação inválida. Por favor selecione a opção desejada.")
