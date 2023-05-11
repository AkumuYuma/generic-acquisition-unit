from overrides import EnforceOverrides
from abc import abstractmethod

class IConfigurationStructure(EnforceOverrides): 
    @abstractmethod
    def loadStructure(self) -> None:  pass

    @abstractmethod
    def checkStructure(self, structure: any) -> bool: pass
