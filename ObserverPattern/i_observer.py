from __future__ import annotations
from abc import ABC, abstractmethod


class IObserver(ABC):
    """
    Interface observer (subscriber)
    """
    
    @abstractmethod
    def update(self, subject) -> None:
        """[summary]

        Args:
            subject (ISubject): Subject object
        """
        pass
