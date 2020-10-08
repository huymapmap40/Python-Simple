from __future__ import annotations
from ObserverPattern.i_observer import IObserver
from ObserverPattern.i_subject import ISubject
from ObserverPattern.concrete_subject import ConcreteSubject


class ConcreteObserverA(IObserver):
    """
    Class concrete IObserver
    """
    
    def update(self, subject: ISubject) -> None:
        if subject._state <= 5:
            print("Observer A: Receive notification from Subject")
            
class ConcreteObserverB(IObserver):
    """
    Class concrete IObserver
    """
    
    def update(self, subject: ISubject) -> None:
        if subject._state > 3:
            print("Observer B: Receive notification from Subject") 

