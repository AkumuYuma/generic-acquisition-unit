from overrides import override
from typing import Dict

from Configuration.Concretes.CGeneralSettingsConfigurationObject import CGeneralSettingsConfigurationObject
from Configuration.Concretes.CGenericModuleConfigurationObject import CGenericModuleConfigurationObject
from Configuration.Concretes.CConcreteUnitConfigurationStructure import CConcreteUnitConfigurationStructure
from Configuration.Concretes.CMappingConfiguration import CMappingConfiguration

class CConcreteUnitConfiguration(CMappingConfiguration): 

    def getGeneralUnitConfiguration(self) -> CGeneralSettingsConfigurationObject:
        self._configuration.get(CConcreteUnitConfigurationStructure.GENRAL_SETTINGS.FIELD)
        
    def getModuleConfigurationByName(self, moduleName: str) -> CGenericModuleConfigurationObject: 
        self._configuration.get(CConcreteUnitConfigurationStructure.MODULES_FIELD).get(moduleName)
