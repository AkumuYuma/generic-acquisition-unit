from abc import abstractmethod
from overrides import EnforceOverrides

from typing import Dict

class IMappingConfiguration(dict, EnforceOverrides): 

    @abstractmethod
    def loadFromDict(self, configDict: Dict[str, any]) -> bool: pass 