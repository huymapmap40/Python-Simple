from ObserverPattern.concrete_subject import ConcreteSubject
from ObserverPattern.concrete_observer import ConcreteObserverA, ConcreteObserverB


if __name__ == "__main__":
    
    # Init subject
    subject = ConcreteSubject()
    
    # Init 2 observer and subscribe to subject
    observerA = ConcreteObserverA()
    observerB = ConcreteObserverB()
    subject.attach(observerA)
    subject.attach(observerB)
    
    # Subject do something event
    subject.some_business_logic()    
