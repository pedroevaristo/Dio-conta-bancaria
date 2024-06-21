from Controller.deposit import depositing_In_Account

class Options_From_View:

    def putting_Information_Of_Depositing(self):
        print("Digite as informações para o deposito")
        name_Person = input("Nome: ")
        value_Deposit = input("Valor do deposito: ")
        verifing_Depoist= depositing_In_Account(name='name_Person',transaction='value_Deposit')
        if verifing_Depoist:
            print("Depositado na sua conta")
        else:
            print("Houve um problema no deposito a sua conta")

    def View_Extract(self):
        print("Buscar diretamente no banco de dado por meio de crud chamando a instancia")
    
    def taking_Withdraw(self):
        print("Pedir infoamção do nome completo")

    
