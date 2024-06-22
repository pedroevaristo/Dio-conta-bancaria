from data.db import Connection, Database

class _Information_Of_Account(Connection):
    Historic_Transaction = Database.get_All_Transactions()
    if not Historic_Transaction:
        print("Nenhuma Transação encontrada")
    for index in Historic_Transaction:
        value_Historic = index["transaction_money"]
        print(f"{value_Historic}")
    