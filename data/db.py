
from Model.bank_account import person
class connection:#Singleton connection
    _instance = None
    _connection = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(connection, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def Connection_With_Database(self):
        if not list_Account:
            self.Connection_With_Database = list_Account = []
        return self.Connection_With_Database



    ''''def remove_added_Information(self, id):
        if id in self.size_list:
            self.size_list.remove(id)'''