from overrides import override, final
from typing import List, Dict

from ruamel.yaml import yaml_object, Node
from ruamel.yaml.comments import CommentedMap

from Configuration.Concretes.CGenericModuleConfiguration import CGenericModuleConfiguration
from SettingsLoader.Concretes.CConfigurationLoader import CConfigurationLoader

@yaml_object(CConfigurationLoader.yamlParser)
@final 
class CCustomModuleConfiguration(CGenericModuleConfiguration): 
    """This class represents the configuration for a generic custom module. It can be instantiated with an arbitrary 
    set of parameters. Those parameters will be initialized as class field. 
    If this class is insantiated from outside (read from yaml configuration), each parameter in the yaml node will correspond to 
    a class field. 
    For this reason, each client of this class must call the method selectNeededParameters in order to choose the actually needed 
    parameters and their default values. 
    """
    
    yaml_tag = "!CCustomModuleConfiguration"
    
    def __init__(self, moduleType: str, inputDataFlows: List[str], outputDataFlows: List[str], **kwargs) -> None:
        super().__init__(moduleType, inputDataFlows, outputDataFlows)
        self._moduleType : str = moduleType
        self._inputDataFlows : List[str] = inputDataFlows 
        self._outputDataFlows : List[str] = outputDataFlows

        # Need to keep in memory a map of the parameter names 
        self.kwargs = kwargs 

        # This is needed to access the parameters from the outside with the names chosen in the constructor kwargs
        self._updateDictAttributeWithKwargs()
    
    @classmethod
    @override
    @final
    def buildCommentedMapFromNode(cls, node: Node) -> CommentedMap: 
        data = super().buildCommentedMapFromNode(node) 
        for argumentName in node.kwargs: 
            data[argumentName] = node.kwargs.get(argumentName)
        return data

    def selectNeededParameters(self, neededParams: Dict[str, any]) -> None: 
        """Selects the needed params of the configuration

        Args:
            neededParams (Dict[str, any]): Dictionary with the needed params. The pairs are <param-name, param-default-value>
        """
        # If a parameter is not among the class field, add it 
        self.kwargs = { key:value for key,value in neededParams.items() if key in neededParams }
        # Kwargs must contain only the params in neededParams (if a param is in kwargs but not needed, remove it)
        self.kwargs = { key:value for key,value in self.kwargs.items() if key in neededParams }
        self._updateDictAttributeWithKwargs()


    def _updateDictAttributeWithKwargs(self) -> None: 
        for customParam in self.kwargs: 
            self.__dict__[customParam] = self.kwargs.get(customParam)