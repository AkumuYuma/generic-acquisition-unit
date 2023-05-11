from overrides import override

from Configuration.Concretes.CMapConfigurationStructureBase import CMapConfigurationStructureBase
from Configuration.Concretes.CGeneralSettingsConfigurationObject import CGeneralSettingsConfigurationObject

class CConcreteUnitConfigurationStructure(CMapConfigurationStructureBase): 

    GENERAL_SETTINGS_FIELD = "GeneralSettings"
    DATAFLOWS_FIELD = "DataFlows"
    MODULES_FIELD = "Modules"

    @override
    def loadStructure(self) -> None:
        self._fieldsStructure = {
          self.GENERAL_SETTINGS_FIELD: type(CGeneralSettingsConfigurationObject()),
          self.DATAFLOWS_FIELD: type(dict()), 
          self.MODULES_FIELD: type(dict())
        }

