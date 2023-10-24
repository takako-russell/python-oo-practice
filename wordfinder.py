"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...

    def __init__(self, path): 
        
        output_file = open(path)
        self.words = self.listwors(self, output_file)
        print(f"{len(self.words)} words read")

    def __repr__(self) 

    def listwords(self, output_file):
       return [w.strip() for w in output_file] 
    

    def random (self):
        return random.choice(self.words)
    

    
class SpecialWordFinder(WordFinder):
    def listwords(self, output_file):
       return [w.strip() for w in output_file if w.strip() and not w.startswith("#")]
        