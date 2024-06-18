#Singleton
from Model.bank_account import person
class connection:
    _instance = None
    size_list =[]
    #verificar se existe uma nova instancia 
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            
        return cls._instance

    #daqui apra baixo é "crud"
    def add_Infor(self, person):
        self.size_list.append(person)

    def get_Extract(self):
        return self.size_list
    
    ''''def remove_added_Information(self, id):
        if id in self.size_list:
            self.size_list.remove(id)'''