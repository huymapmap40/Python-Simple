from __future__ import annotations
from ObserverPattern.i_subject import ISubject
from ObserverPattern.i_observer import IObserver
from random import randrange
from typing import List


class ConcreteSubject(ISubject):
    """
    Class concrete ISubject
    """
    
    _state: int = None
    _observers: List[IObserver] = []
    
    def attach(self, observer: IObserver) -> None:
        print("Subject: Attached an observer")
        self._observers.append(observer)

    def detach(self, observer: IObserver) -> None:
        print("Subject: Detach an observer")
        self._observers.remove(observer)
        
    def notify(self) -> None:
        print("Subject: Notifying to obserers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self):
        print("\nDo some business work")
        self._state = randrange(0, 10)
        print(f"Subject: state had changed to {self._state}")
        self.notify()