import random
saques = 500
class Conta:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0.0

    def verificar_senha(self, senha):
        return self.senha == senha

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque!")
        elif valor > saques:
            print("Limite de saque de R$500 ultrapassado!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

class Banco: 
    def __init__(self):
        self.contas = {}
    
    def criar_conta(self):
        nome = input("\nDigite o nome do titular: ")
        senha = input("Digite a senha do titular: ")
        numero = random.randint(10000, 99999)
        while numero in self.contas:
            numero = random.randint(10000, 99999)
        conta = Conta(numero, nome, senha)
        self.contas[numero] = conta
        print(f"Conta criada com sucesso! Número da conta: {numero}")

    def acessar_conta(self):
        numero = int(input("\nDigite o número da conta: "))
        senha = input("Digite a senha da conta: ")
        conta = self.contas.get(numero)

        if conta and conta.verificar_senha(senha):
            self.menu_conta(conta)
        else:
            print("Número ou senha inválidos! Tente novamente")

    def menu_conta(self,conta):
        while True:
            print("\nMENU DA CONTA:")
            print("[1] - Depositar")
            print("[2] - Sacar")
            print("[3] - Exibir Saldo")
            print("[4] - Sair")
            opcao = int(input("Escolha uma opção: "))   
            
            if opcao == 1:
                valor = float(input("Digite o valor do depósito: "))
                conta.depositar(valor)
            
            elif opcao == 2:
                valor = float(input("Digite o valor do saque: "))
                conta.sacar(valor)

            elif opcao == 3:
                conta.exibir_saldo()
            
            elif opcao == 4:
                print("Encerrando acesso à conta...")
                break

            else:
                print("Opção inválida, tente novamente!")

banco = Banco()

while True:
    print("\n=== BEM-VINDO AO BANCO UNIDESC ===")
    print("[1] - Criar Conta")
    print("[2] - Acessar Conta")
    print("[3] - Sair")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        banco.criar_conta()
    elif escolha == 2:
        banco.acessar_conta()
    elif escolha == 3:
        print("Obrigado por usar o Banco UNIDESC! Saindo...")
        break
    else:
        print("Opção inválida, tente novamente!")