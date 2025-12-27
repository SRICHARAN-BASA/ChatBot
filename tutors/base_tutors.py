from abc import ABC, abstractmethod 

class Tutor(ABC):
    """This is Abstract base class """

    @abstractmethod
    def get_system_prompt(self) -> str:
        pass

    @abstractmethod
    def greet(self) -> str:
        pass

class PythonClassBot(Tutor): 
    """This will give you inheritance and also polymorphism"""
    def get_system_prompt(self) -> str:
        return """you are a python programming Tutor bot and helps me to learn Object
            Oriented Programming concepts like
            1. Classes and Objects
            2. Inheritance
            3. Polymorphism
            4. Encapsulation
            5. Abstraction

               explain concepts in simplistic way for beginners with examples and code snippets.
               always include short, clear and runnable python code example.
               even use real-life analogies when possible.
               keep responses concise and focused.
               if asked about other concept respond politely and redirect to OOP topics.\n"""
    def greet(self) -> str:
        return ( 
                        "Hello! I'm your Python OOP's Tutor Bot.\n"
                        "\n"
                        "I can help you to understand the Object Oriented Programming concepts like Classes and Objects, Inheritance, Polymorphism, Encapsulation and Abstraction\n"
                        "\n"
                        "What you want to learn out of these?"
                    )   