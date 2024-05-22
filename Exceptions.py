class NoResults(Exception):
    def __init__(self, message):
        self.message=message
        super().__init__(self.message)

class WrongChoiceException(Exception):
    def __init__(self, message):
        self.message=message
        super().__init__(self.message)


