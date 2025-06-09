def sistema_bancario():

    menu = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """

    
    saldo = 0.0
    limite_saque_valor = 500.0
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES_DIARIOS = 3

    print("\nBem-vindo ao nosso banco!")

    while True:
        
        opcao = input(menu).lower()

       
        if opcao == 'd':
            print("\n--- Depósito ---")
            try:
                valor_deposito = float(input("Informe o valor do depósito: R$ "))

                if valor_deposito > 0:
                    saldo += valor_deposito
                  
                    extrato += f"Depósito:\t\tR$ {valor_deposito:.2f}\n"
                    print(f"✅ Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
                else:
                    print("❌ Operação falhou! O valor informado é inválido. Tente novamente.")

            except ValueError:
                print("❌ Operação falhou! Por favor, insira um valor numérico.")

        # Operação de Saque 
        elif opcao == 's':
            print("\n--- Saque ---")
            try:
                valor_saque = float(input("Informe o valor do saque: R$ "))

               
                excedeu_saldo = valor_saque > saldo
                excedeu_limite_valor = valor_saque > limite_saque_valor
                excedeu_limite_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

                if excedeu_saldo:
                    print(f"❌ Operação falhou! Você não tem saldo suficiente. Saldo atual: R$ {saldo:.2f}")

                elif excedeu_limite_valor:
                    print(f"❌ Operação falhou! O valor do saque excede o limite de R$ {limite_saque_valor:.2f} por transação.")

                elif excedeu_limite_saques:
                    print(f"❌ Operação falhou! Número máximo de {LIMITE_SAQUES_DIARIOS} saques diários excedido.")

                elif valor_saque > 0:
                    saldo -= valor_saque
                    numero_saques += 1
                    
                    extrato += f"Saque:\t\t\tR$ {valor_saque:.2f}\n"
                    print(f"✅ Saque de R$ {valor_saque:.2f} realizado com sucesso!")

                else:
                    print("❌ Operação falhou! O valor informado é inválido.")

            except ValueError:
                print("❌ Operação falhou! Por favor, insira um valor numérico.")

        # Operação de Extrato 
        elif opcao == 'e':
            print("\n================ EXTRATO ================")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                print(extrato)
            
            print(f"\nSaldo atual:\t\tR$ {saldo:.2f}")
            print("==========================================")

        # Opção de Sair 
        elif opcao == 'q':
            print("\nObrigado por usar nosso sistema. Até logo! 👋\n")
            break

       
        else:
            print("❌ Operação inválida, por favor selecione novamente a operação desejada.")



if __name__ == "__main__":
    sistema_bancario()