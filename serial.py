"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    """Create a new instance of the class and initial starting number is 0"""
    def __init__(self, start=0):
        self.start = self.next = start

    """Show representation"""
    def __repr__(self):
       return f"<SerialGenerator start = {self.start} next = {self.next}>"
    

    """Increment the current number by 1 and return the number"""
    def generate(self):
     self.next += 1
     return self.next - 1

    """Reset the current generated number to the inital starting number"""
    def reset(self):
       self.next = self.start
        


