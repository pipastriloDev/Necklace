class Necklace(object):
    """ Simulation of a bead necklace where you can flip the letters around the string"""
    def __init__(self,string:str):
        self.word= string


    def flip_backwards(self):
        """ Saves the word on necklace with the last letter moved to the front e.g. Nicole > eNicol"""
        self.word = f"{self.word[-1::]}{self.word[0:-1:]}"
    
    def flip_forward(self):
        """Saves the word on the necklace with the first letter moved to be the last Nicole > icoleN"""
        self.word = f"{self.word[1::]}{self.word[0:1:]}"
    def get_word(self):
        return self.word

    def matcher(stringA, stringB):
        """returns if two strings could be on the same necklace"""  
        match = False
        necklace = Necklace(stringA)
        length = len(stringA)
        while length >0:
            necklace.flip_forward()
            if necklace.get_word() == stringB:
                match = True
            length += -1
        print(match)

        

Necklace.matcher("estingtt", "ttesting")
