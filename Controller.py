class Controller:
    def __init__(self, body, env):
        self.environment = env
        self.body = body
        self.body.controller = self
        self.collected = 0
        self.stay = [0, 0]
        self.up = [0, 1]
        self.right = [1, 0]
        self.down = [0, -1]
        self.left = [-1, 0]
        self.heading = None
        self.new_mov = 0
        self.next_mov = None
        
    def goToNext(self):
        moved = False
        while not moved:
            if new_pos == 1:
                self.body.move(next_pos)
                moved = True
            else:
                getNext()
    

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
