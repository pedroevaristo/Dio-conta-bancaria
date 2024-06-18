#Singleton
class connection:
    _instance = None
    size_list =[]

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            
        return cls._instance

    #daqui apra baixo é "crud"
    def addInfor(self, name, valueMoney):
        self.size_list.append(name, valueMoney)

    def get_added_Information(self):
        return self.size_list
    
    ''''def remove_added_Information(self, id):
        if id in self.size_list:
            self.size_list.remove(id)'''