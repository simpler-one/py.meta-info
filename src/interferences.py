from abc import ABC, abstractmethod


class OnInherit(ABC):
    @abstractmethod
    def on_inherit(self, parent):
        raise NotImplementedError()
