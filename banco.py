import textwrap

def menu():
    
    menu_text = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_text))

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

  
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
   
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return None

def listar_contas(contas):
    
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return

    print("================ CONTAS ================")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))
    print("========================================")

def main():
   
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []
    

    estado_contas = {}

    while True:
        opcao = menu()

        if opcao == "d":
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)
            
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                
                
                estado_contas.setdefault(numero_conta, {'saldo': 0.0, 'extrato': "", 'numero_saques': 0})
                
                
                saldo_atual = estado_contas[numero_conta]['saldo']
                extrato_atual = estado_contas[numero_conta]['extrato']
                
                saldo_atual, extrato_atual = depositar(saldo_atual, valor, extrato_atual)
                
                estado_contas[numero_conta]['saldo'] = saldo_atual
                estado_contas[numero_conta]['extrato'] = extrato_atual
            else:
                print("\n@@@ Conta não encontrada! @@@")

        elif opcao == "s":
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)

            if conta:
                valor = float(input("Informe o valor do saque: "))
                
             
                estado_contas.setdefault(numero_conta, {'saldo': 0.0, 'extrato': "", 'numero_saques': 0})
                
                estado = estado_contas[numero_conta]
                
                estado['saldo'], estado['extrato'], estado['numero_saques'] = sacar(
                    saldo=estado['saldo'],
                    valor=valor,
                    extrato=estado['extrato'],
                    limite=500, # Limite fixo por saque
                    numero_saques=estado['numero_saques'],
                    limite_saques=LIMITE_SAQUES,
                )
            else:
                print("\n@@@ Conta não encontrada! @@@")

        elif opcao == "e":
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c['numero_conta'] == numero_conta), None)

            if conta:
               
                estado = estado_contas.get(numero_conta, {'saldo': 0.0, 'extrato': ""})
                exibir_extrato(estado['saldo'], extrato=estado['extrato'])
            else:
                print("\n@@@ Conta não encontrada! @@@")

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            nova_conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if nova_conta:
                contas.append(nova_conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nObrigado por usar nosso sistema. Até logo! 👋\n")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()