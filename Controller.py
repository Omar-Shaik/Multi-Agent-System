class Controller:

    def __init__(self, body):
        self.up = [0, 1]
        self.right = [1, 0]
        self.down = [0, -1]
        self.left = [-1, 0]
        self.body = body
        self.body.controller = self 
    
    def scanner(self):
        return self.body.env.objectsAround(self)


#Each type of controller will do something differnt with the list of objects around it
class CompetitiveController(Controller):
        
        def __init__(self):
        
        
        def radar(self):
            
            
        def nextMove(self):       
        
class CollaborativeController(Controller):

        def __init__(self):
        
        
        def radar(self):
            
        
        def nextMove(self)
        

class CompassionateController(Controller):
        
        def __int__(self):
        
        
        def radar(self):
            
        
        def nextMove(self):
        
