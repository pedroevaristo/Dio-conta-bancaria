
from typing import Any
from Model.bank_account import person
class connection:#Singleton connection
    _instance = None
    _connection = None
    def __call__(self, *args, **kwds):

        if cls._instance is None:
            cls._instance = super(connection, cls).__call__(cls, *args, **kwargs)
        return cls._instance
    
class Connection_With_Database(metaclass=connection):
   _connection=None
   def connection(self):
        if not list_Account:
            self.Connection_With_Database = list_Account = []
            self.Connection_With_Database = transactions_ = {}
        return self.Connection_With_Database

    #def transfering_Money:
        

    ''''def remove_added_Information(self, id):
        if id in self.size_list:
            self.size_list.remove(id)'''