#interface metodo abstrato
from abc import ABC, abstractmethod
import bank_account

class functions(ABC):
    @abstractmethod
    def execute_Task(self):
        pass
    
#depois de colcoar as três informações colcoar no final em um lista ou dictionary