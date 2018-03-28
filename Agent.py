import Object as obj
import Controller as con

class Agent:
    def __init__(self, env, x, y, type):
        self.body = obj.Body(env, x, y, type)
        self.controller = con.Controller(self.body)
        self.channels = []
        self.new_messages = []
        self.collected_count = 0
        self.heading = []
        self.next_move = []
        
    def sendMessage(self, channel, message):
        channel.sendMessage(self, message)
        
    def readNewMessage(self):
        for i in self.new_messages:
            #read message
        self.new_messages.del(i)
        
    def radarSensor(self):
        self.controller.scan()
