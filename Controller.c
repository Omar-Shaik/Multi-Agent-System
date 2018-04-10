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
    
    def getNext(self):
        got_next = False
        if heading is None:
            got_next = False
            while not got_next:
                pos = [self.body.position[0] + random.randint(0, 1), self.body.position[1] + random.randint(0, 1)]
                got_next = validPosition(pos)
            next_mov = pos
            new_mov = 1
        else:    
            if self.heading[0] - self.body.position[0] != 0:
                if self.heading[0] - self.body.position[0] > 0:
                    if self.env.validPosition([self.body.position[0] + self.right[0], self.body.position[1] + self.right[1]):
                        self.next_mov = self.right 
                else:
                    if self.env.validPosition([self.body.position[0] + self.left[0], self.body.position[1] + self.left[1]):
                        self.next_mov = self.left
           elif self.heading[1] - self.body.position[1] != 0:
                if self.heading[1] - self.body.position[1] > 0:
                    if self.env.validPosition([self.body.position[0] + self.up[0], self.body.position[1] + self.up[1]):
                        self.next_mov = self.up
                else:
                    if self.env.validPosition([self.body.position[0] + self.down[0], self.body.position[1] + self.down[1]):
                        self.next_mov = self.down
           else:
                next_mov = self.stay
           new_mov = 1
        
        

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
