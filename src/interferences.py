from abc import ABC, abstractmethod


class OnDecorate(ABC):
    @abstractmethod
    def on_decorate(self, target, name):
        """
        Handle OnDecorate event
        :param Any target:
        :param str name:
        :return:
        """
        raise NotImplementedError()


class OnInherit(ABC):
    @abstractmethod
    def on_inherit(self, parent):
        """
        Handle OnInherit event
        :param Any parent: parent class info
        """
        raise NotImplementedError()
