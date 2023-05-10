from overrides import override, final

from ruamel.yaml import Constructor, Node, Representer
from ruamel.yaml.comments import CommentedMap

from Configuration.Interfaces.IConfigurationObject import IConfigurationObject

class CMappingConfigurationObjectBase(IConfigurationObject): 
    """The base class from Mapping Configuration Objects. 
    Implements the to_yaml and from_yaml for this kind of objects. 
    The derived classes only has to implement their constructor and the buildCommentedMapFromNode method.
    """

    @classmethod 
    @override
    @final 
    def to_yaml(cls, representer: Representer, node: Node) -> Node: 
        data = cls.buildCommentedMapFromNode(node)
        return representer.represent_mapping(cls.yaml_tag, data)
    
    @classmethod
    @override
    @final
    def from_yaml(cls, constructor: Constructor, node: Node) -> IConfigurationObject: 
        data = CommentedMap()
        constructor.construct_mapping(node, data, deep=True)
        return cls(**data)