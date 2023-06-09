from io import FileIO
import os
from typing import Dict

from ruamel.yaml import YAML
from overrides import override

from SettingsLoader.Interfaces.IConfigurationLoader import IConfigurationLoader
from Configuration.Interfaces.IConfigurationObject import IConfigurationObject
from Configuration.Concretes.CConcreteUnitConfiguration import CConcreteUnitConfiguration

class CConfigurationLoader(IConfigurationLoader): 
    yamlParser = YAML() 

    def __init__(self, configurationDirectory: str, configurationFileName: str) -> None:
        super().__init__()

        configFullPath = configurationDirectory and os.path.join(configurationDirectory, configurationFileName)
        self._checkConfigPath(configFullPath)

        self._configFullPath : str = configFullPath

        self._stream : FileIO = self._openAndReturnFileStream(self._configFullPath)
        self._configurationStructure : CConcreteUnitConfiguration = CConcreteUnitConfiguration()
        self._configuration : Dict[str, any] = {}
    
    def __del__(self) -> None: 
        self._stream.close()

    @property 
    def configuration(self) -> CConcreteUnitConfiguration: return self._configuration

    @override
    def loadConfiguration(self) -> None: 
        self._configurationStructure.loadStructure()
        if self._stream is not None: 
            self._configuration = self.yamlParser.load(self._stream)
            if not self._configurationStructure.checkConfiguration(self._configuration): 
                raise IOError("The configuration structure is incorrect")
    
    def dumpObject(self, objectToDump: IConfigurationObject) -> None: 
        self.yamlParser.dump(objectToDump, self._stream)
        
    def _checkConfigPath(self, configPath: str) -> None: 
        if not configPath: 
            errorMessage = (f"The configuration directory does not contain the configuration file")
            raise IOError(errorMessage)
        print(f"Configuration path: {configPath}")
        
    def _openAndReturnFileStream(self, path: str) -> FileIO: 
        try: 
            return open(path, "r+") 
        except IOError as e: 
            errorMessage = f"Cannot open configuration file, details: {e.strerror}"
            raise IOError(errorMessage)