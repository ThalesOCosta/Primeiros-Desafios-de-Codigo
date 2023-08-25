"""
-------------------------------------------------------------------------------------------
Desafio
Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a 
realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito 
e verificar se o valor é válido. Se o valor for maior do que zero, o programa deve adicionar 
o valor ao saldo da conta. Caso contrário, o programa deve exibir uma mensagem de erro e 
solicitar um novo valor. O programa deve continuar solicitando valores de depósito até que 
seja digitado um valor válido.

-------------------------------------------------------------------------------------------
Entrada
O programa deve utilizar o Scanner para receber os valores de depósito digitados pelo 
cliente. Os valores podem ser decimais, representando valores em reais.

-------------------------------------------------------------------------------------------
Saída
O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for 
informado e o saldo da conta for atualizado. Caso um valor inválido seja digitado, o 
programa deve exibir uma mensagem de erro e solicitar um novo valor.

-------------------------------------------------------------------------------------------
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas 
esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

-------------------------------------------------------------------------------------------
Entrada:
    500.50

Saída:
    Deposito realizado com sucesso!
    Saldo atual: R$ 500.50

-------------------------------------------------------------------------------------------
Entrada:
    -100

Saída:
    Valor invalido! Digite um valor maior que zero.

-------------------------------------------------------------------------------------------
Entrada:
    0

Saída:
    Encerrando o programa...
-------------------------------------------------------------------------------------------
"""
saldo = float(0)

while True:
    valor = float(input("Valor: "))
    
    if valor > 0:
        # TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
        saldo += valor
        print(f"Deposito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        
    elif valor == 0:
        # TODO: Imprimir a mensagem de valor inválido.
        print("Encerrando o programa...")
        break
    else:
        # TODO: Imprimir a mensagem de encerrar o programa.
        print("Valor invalido! Digite um valor maior que zero.")
