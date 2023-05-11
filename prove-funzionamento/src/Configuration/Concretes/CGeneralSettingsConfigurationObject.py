from overrides import override, final

from ruamel.yaml import CommentedMap, Node

from Configuration.Concretes.CMappingConfigurationObjectBase import CMappingConfigurationObjectBase

class CGeneralSettingsConfigurationObject(CMappingConfigurationObjectBase): 
    yaml_tag = "!CGeneralSettingsConfigurationObject"
    
    def __init__(self, unitName: str = "", unitDescription: str = ""):
      self._unitName : str = unitName
      self._unitDescription : str = unitDescription
  
    @property
    def unitName(self) -> str: return self._unitName
    @property 
    def unitDescription(self) -> str: return self._unitDescription
  
    @classmethod 
    @override
    @final 
    def buildCommentedMapFromNode(cls, node: Node) -> CommentedMap: 
        data = CommentedMap()
        data["unitName"] = node.unitName
        data["unitDescription"] = node.unitDescription 
        return data
        