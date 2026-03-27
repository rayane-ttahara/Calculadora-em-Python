while True:
    print("\n--- CALCULADORA ---")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Saindo...")
        break

    if opcao in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = num1 + num2

        elif opcao == "2":
            resultado = num1 - num2

        elif opcao == "3":
            resultado = num1 * num2

        elif opcao == "4":
            if num2 == 0:
                print("Erro: divisão por zero!")
                continue
            resultado = num1 / num2

        print(f"Resultado: {resultado}")

    else:
        print("Opção inválida!")