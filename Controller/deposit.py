#Factory Method
from data.db import connection
from Model.bank_account import person
from Model.interface import functions

class depositing_In_Account(name, transaction):
    
    connection.Connection_With_Database