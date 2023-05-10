from abc import abstractclassmethod

from overrides import EnforceOverrides

class IConfigurationLoader(EnforceOverrides): 
    @abstractclassmethod
    def loadConfiguration(self) -> None: 
        pass