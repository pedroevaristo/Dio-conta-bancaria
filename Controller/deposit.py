#Factory Method
from data.db import Connection, Database

class depositing_In_Account(Connection):
    print("Digite as informações para o deposito")
    name_Person = input("Nome: ")
    value_Deposit = input("Valor do deposito: ")

    verifing_Depoist = Database(name_Person, value_Deposit)

    if verifing_Depoist:
        print("Depositado na sua conta")
    else:
        print("Houve um problema no deposito a sua conta")
