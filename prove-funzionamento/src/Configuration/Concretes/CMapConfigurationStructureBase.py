from typing import Dict, List
from overrides import override

from Configuration.Interfaces.IConfigurationStructure import IConfigurationStructure


class CMapConfigurationStructureBase(IConfigurationStructure):

    def __init__(self) -> None:
        # Dictionary where the pairs are <name_of_the_field, type_of_the_field>
        self._fieldsStructure: Dict[str, any] = None 

    @override
    def checkStructure(self, structure: any) -> bool:
        if self._fieldsStructure is None: 
            return False 
        if not self._fieldsStructure.keys() == structure.keys(): 
            return False 
        for fieldName, fieldType in self._fieldsStructure.items(): 
            if type(structure.get(fieldName)) != fieldType: 
                return False 
        return True 

    def getConfigurationFieldNames(self) -> List[str]: 
        if self._fieldsStructure is None: 
            return None 
        return list(self._fieldsStructure.keys())

    def getFieldTypeFromName(self, fieldName) -> type: 
        if self._fieldsStructure is None: 
            return None 
        return self._fieldsStructure.get(fieldName)
            