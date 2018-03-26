
class Agent:

    def __init__(self, env, x, y, type):
        self.body = Body(env, x, y, type)
        self.controller = Controller(self.body)
        self.channels = []
        self.new_messages = []
        self.collected_count = 0
        self.heading = []
        self.next_move = []
        
    def sendMessage(channel, message):
        channel.send_message(self, message)
        
    def readNewMessage(self):
        for i in self.new_messages:
            #read message
        self.new_messages.del(i)
