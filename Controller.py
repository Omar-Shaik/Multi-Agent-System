class Controller:
    def __init__(self, body):
        self.up = [0, 1]
        self.right = [1, 0]
        self.down = [0, -1]
        self.left = [-1, 0]
        self.collected = 0
        self.body = body
        self.body.controller = self

    def scanner(self):
        return self.body.env.objectsAround(self)

    def radar(self):
        return 0

    def nextMove(self):
        return 0

class Competitive_Controller(Controller):
    def __init__(self, body):
        Controller.__init__(self, body)
        x = 1

class Collaborative_Controller(Controller):
    def __init__(self, body):
        Controller.__init__(self, body)
        x = 1

class Compassionate_Controller(Controller):
    def __init__(self, body):
        Controller.__init__(self, body)
        x = 1
        
