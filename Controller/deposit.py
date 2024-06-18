#Factory Method
from data.db import connection
from Model.bank_account import person
from Model.interface import functions
class depositing_Amount(functions):
    func1 = functions()
    def __init__(self, amount):
        self.amount = amount
    
    def execute_Task(self,name,_value):
        name_Person = name
        amountFromReceiver = _value
        = person(name=name_Person,amount=amountFromReceiver) #fazer de alguma forma repassa as informações
