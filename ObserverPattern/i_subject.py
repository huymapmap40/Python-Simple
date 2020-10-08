from __future__ import annotations
from abc import ABC, abstractmethod
from ObserverPattern.i_observer import IObserver


class ISubject(ABC):
    """ Interface Subject (publisher)

    Args:
        ABC: Helper class that provides a standard way to create an ABC using
        inheritance.
    """

    @abstractmethod
    def attach(self, observer: IObserver) -> None:
        """ Method attach observer to the subject

        Args:
            observer (IObserver): observer object
        """
        pass
    
    @abstractmethod
    def detach(self, observer: IObserver) -> None:
        """ Method detach observer out of subject

        Args:
            observer (IObserver): observer object
        """
        pass
        
    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about events
        """
        pass
