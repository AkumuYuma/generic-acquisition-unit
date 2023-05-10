from __future__ import annotations
from abc import abstractclassmethod

from overrides import EnforceOverrides
from ruamel.yaml import Constructor, Node, Representer, CommentedMap


class IConfigurationObject(EnforceOverrides): 
    """Interface to represent a configuration object to input/output with yaml configuration file. 
    """

    @classmethod
    @abstractclassmethod
    def buildCommentedMapFromNode(node: Node) -> CommentedMap: 
        """Builds and returns a CommentedMap with info contained in the node object. Each Configuration object must implement this method in order to 
        describe the way the oject must be deserialized from the yaml node.

        Args:
            node (Node): The node to deserialize 

        Returns:
            CommentedMap: The deserialized data
        """
        pass 

    @classmethod
    @abstractclassmethod
    def to_yaml(cls, representer: Representer, node: Node) -> Node: 
        """Serializes the object of the class into a yaml node. 

        Args:
            representer (Representer): The node builder.
            node (Node): The data structure where the object specific fields are stored.

        Returns:
            Node: The node to dump in the yaml file. 
        """
        pass 

    @classmethod
    @abstractclassmethod
    def from_yaml(cls, constructor: Constructor, node: Node) -> IConfigurationObject: 
        """Creates an object of this class from a yaml node. 

        Args:
            constructor (Constructor): The node-class converter
            node (Node): The yaml read node

        Returns:
            IConfigurationObject: The object created
        """
        pass 
