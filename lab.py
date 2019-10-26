"""Classes for object attributes lab."""

class Person:
    """Person class."""
    def __init__(self, first: str, last: str):
        self.first = first
        self.last = last

class Driver(Person):
    """Driver class."""
    def __init__(self, first: str, last: str, **kwargs):
        Person.__init__(self,first, last)
        self.miles_driven = kwargs.get('miles_driven', 0)
        self.rating = kwargs.get('rating', None)

    def greet_passenger(self):
        """Greet the passenger."""
        return f"Hello! I'll be your driver today. My name is {self.first} {self.last}."

class Passenger(Person):
    """Passenger class."""

    def yell_name(self):
        print(f"{self.first.upper()} {self.last.upper()}")
