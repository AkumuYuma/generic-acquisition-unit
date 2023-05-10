from overrides import override
from typing import List

from ruamel.yaml import yaml_object, Node
from ruamel.yaml.comments import CommentedMap

from Configuration.Concretes.CMappingConfigurationObjectBase import CMappingConfigurationObjectBase
from SettingsLoader.Concretes.CConfigurationLoader import CConfigurationLoader

@yaml_object(CConfigurationLoader.yamlParser)
class CGenericModuleConfiguration(CMappingConfigurationObjectBase): 
    """The Generic Module Configuration Object. It implements the base configuration needed from any module:\n
    -moduleType: The name of the class of the module\n
    -inputDataFlows
    -outputDataFlows
    """

    yaml_tag = '!CGenericModuleConfiguration'

    def __init__(self, moduleType: str, inputDataFlows: List[str], outputDataFlows: List[str]) -> None:
        super().__init__()
        self._moduleType : str = moduleType
        self._inputDataFlows : List[str] = inputDataFlows 
        self._outputDataFlows : List[str] = outputDataFlows
    
    @property
    def moduleType(self) -> str: return self._moduleType
    @property 
    def inputDataFlows(self) -> List[str]: return self._inputDataFlows
    @property 
    def outputDataFlows(self) -> List[str]: return self._outputDataFlows

    @classmethod
    @override
    def buildCommentedMapFromNode(cls, node: Node) -> CommentedMap: 
        data = CommentedMap()
        data["moduleType"] = node.moduleType
        data["inputDataFlows"] = node.inputDataFlows 
        data["outputDataFlows"] = node.outputDataFlows
        return data
    