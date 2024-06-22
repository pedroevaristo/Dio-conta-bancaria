class Connection: #Singleton connection
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Connection, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    
class Database(Connection):
    def __init__(self):
        super().__init__()
        self.transactions = []

    def Add_Transaction(self, name, transaction_Money):
        transaction = {"name": name, "transaction_money": transaction_Money}
        return self.transactions.append(transaction)
    
    def get_All_Transactions(self, transaction ):
        return self.transactions