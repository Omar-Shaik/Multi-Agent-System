class Controller:

    def __init__(self, body, type):
        self.up = [0, 1]
        self.right = [1, 0]
        self.down = [0, -1]
        self.left = [-1, 0]
        self.type = type
        self.body = body
        self.body.controller = self 
    
    def scanner(self):
        return self.body.env.objectsAround(self)
    
    def radar(self):
        
    def nextMove(self):
        
