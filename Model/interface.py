#interface metodo abstrato
from abc import ABC, abstractmethod
# resolver o rpoblem de chamar o metedo abstrato para implementar na concreta

class functions(ABC):
    @abstractmethod
    def execute_Task(self):
        pass
    
#depois de colcoar as três informações colcoar no final em um lista ou dictionary