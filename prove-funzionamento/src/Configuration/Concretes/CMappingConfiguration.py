from overrides import override
from typing import Dict

from Configuration.Interfaces.IMappingConfiguration import IMappingConfiguration
from Configuration.Concretes.CMapConfigurationStructureBase import CMapConfigurationStructureBase

class CMappingConfiguration(IMappingConfiguration): 
    def __init__(self) -> None: 
        self._configurationStructure : CMapConfigurationStructureBase = None
        self._configuration : Dict[str, any] 

    @property 
    def configurationStructure(self) -> CMapConfigurationStructureBase: 
        return self._configurationStructure

    @configurationStructure.setter
    def configurationStructure(self, configStructure : CMapConfigurationStructureBase) -> None: 
        self._configurationStructure = configStructure 
        self._configurationStructure.loadStructure() 

    @override 
    def loadFromDict(self, configDict : Dict[str, any]) -> bool: 
        if self._configurationStructure.checkConfiguration(configDict): 
            self._configuration = configDict
            return True 
        return False