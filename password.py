import string, random

class PassWord:
    def __init__(self,length:int,symbols:bool,numbers:bool):
        self.length = length
        self.symbols = symbols
        self.numbers = numbers
        self.password = ""

    def generate(self):

        while self.length >= len(self.password):
            randomAlphabet = string.ascii_letters[random.randrange(52)]
            randomNumber = string.digits[random.randrange(10)] if self.numbers else ""
            randomSymbol = string.punctuation[random.randrange(32)] if self.symbols else ""

            #Password has equal weights for alphabets, digits and symbols
            self.password = self.password + random.choice([randomAlphabet, randomNumber, randomSymbol])

        return self.password
