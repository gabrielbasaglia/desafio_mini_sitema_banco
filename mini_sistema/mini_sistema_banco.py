menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
       
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido!")    

    elif opcao == "s":
      valor = float(input("Digite o valor do saque: "))

      excedeu_saldo = valor > saldo

      excedeu_limite = valor > limite

      excedeu_saque = numero_saques >= LIMITE_SAQUES       


      if excedeu_saldo:
        print("Saldo insuficiente!")

      elif excedeu_limite:
        print("Limite de saques excedido!")

      elif excedeu_saque:
        print("Limite de saques diários excedido!")

      elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1        

      else:
        print("Valor inválido!")

    elif opcao == "e":
        print("\n====================== Extrato ======================\n")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("\n=====================================================\n")

    elif opcao == "q":
        print("Saindo...")
        break 

    else:
        print("Operação inválida, por favor selecione uma opção válida!")        