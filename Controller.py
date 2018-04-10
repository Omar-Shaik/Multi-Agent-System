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
        self.headings = []
        self.new_mov = 0
        self.next_mov = None
        self.stop = False
	self.channels = {}


    def steer(dir):
    	next_mov = dir
        new_mov = 1
    
    			
    def goToNext(self):
        if stop:
            steer(self.stay)
        else:
            moved = False
            while not moved:
                if new_mov == 1:
                    self.body.move(next_mov)
                    moved = True
                    if self.body.position in self.headings:
                        self.headings.rem(self.body.position)
                else:
                    getNext()
    
    	
    def getNext(self):
        if not headings:
            got_next = False
            while not got_next:
                pos = [self.body.position[0] + random.randint(0, 1), self.body.position[1] + random.randint(0, 1)]
                got_next = validPosition(pos)
            steer(pos)
        else:
        	got_next = False
            if self.headings[0][0] - self.body.position[0] != 0:
                if self.headings[0][0] - self.body.position[0] > 0:
                    if self.env.validPosition([self.body.position[0] + self.right[0], self.body.position[1] + self.right[1]):
                        steer(self.right)
                       	got_next = True
                else:
                    if self.env.validPosition([self.body.position[0] + self.left[0], self.body.position[1] + self.left[1]):
                        steer(self.left)
                        got_next = True
            if not got_next:
                if self.headings[0][1] - self.body.position[1] > 0:
                    if self.env.validPosition([self.body.position[0] + self.up[0], self.body.position[1] + self.up[1]):
                        steer(self.up)
                    else:
                        steer(self.stay)
                else:
                    if self.env.validPosition([self.body.position[0] + self.down[0], self.body.position[1] + self.down[1]):
                        steer(self.down)
                    else:
                        steer(self.stay)
                       


class Competitive_Controller(Controller):
	def __init__(self, body, env):
        	Controller.__init__(self, body, env)

	def readMessages(self):
        	for i in new_messages:
            		if i[0] == "head":
                		headings.append(i[1])
            		else:
                		self.stop = True
		
    	def scan(self):
    		visible = self.env.objectsAround(self)

                        
     
class Collaborative_Controller(Controller):
	def __init__(self, body, env):
    		Controller.__init__(self, body, env)

	def readMessages(self):
    		for i in new_messages:
        	if i[0] == "head":
            	headings.append(i[1])
      	
											   
	def scan(self):
    		visible = self.env.objectsAround(self)
        	if self.collected < self.number_of_targets:
            	self.stop = True 
                    
        for i in visible:
        	self.channels[i.object_type].sendMessage(self, ["Head", i.position])


class Compassionate_Controller(Controller):
	def __init__(self, body, env):
    		Controller.__init__(self, body, env)
    
    
	def readMessages(self):
    		for i in new_messages:
        	if i[0] == "head":
            	headings.append(i[1])
        	else:
            	self.stop = True
                
    
	def scan(self):
    		visible = self.env.objectsAround(self)
      		if self.collected < self.number_of_targets:
        		self.stop = True 
          	
		for i in visible:
        		self.channels[i.object_type].sendMessage(self, ["Head", i.position] )
 
