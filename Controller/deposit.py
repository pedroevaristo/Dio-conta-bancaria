#Factory Method
from data.db import connection
from data.db import Connection_With_Database
from Model.bank_account import person
from Model.interface import functions

class depositing_In_Account(self):
    new_Deposit = Connection_With_Database.connection()
    print("Digite as informações para o deposito")

    name_Person = input("Nome: ")

    value_Deposit = input("Valor do deposito: ")
    
    

    if verifing_Depoist:
        print("Depositado na sua conta")
    else:
        print("Houve um problema no deposito a sua conta")