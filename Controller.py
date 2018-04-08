class Controller:
    def __init__(self, body, env):
        self.up = [0, 1]
        self.right = [1, 0]
        self.down = [0, -1]
        self.left = [-1, 0]
        self.collected = 0
        self.body = body
        self.environment = env
        self.body.controller = self
        self.new_pos = 0
        self.next_pos = None
        self.stay = 00
        
    def goToNext(self):
        moved = False
        while not moved:
            if new_pos == 1:
                self.body.move(next_pos)
                moved = True
            else:
                getNext()
            
        
        

    def scanner(self):
        return self.body.env.objectsAround(self)

    def radar(self):
        return 0

    def nextMove(self):
        return 0

class Competitive_Controller(Controller):
    def __init__(self, body, env):
        Controller.__init__(self, body, env)
        x = 1

class Collaborative_Controller(Controller):
    def __init__(self, body, env):
        Controller.__init__(self, body, env)
        x = 1

class Compassionate_Controller(Controller):
    def __init__(self, body, env):
        Controller.__init__(self, body, env)
        x = 1
