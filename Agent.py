import Object
import Controller


class Agent:
    def __init__(self, env, x, y, target_type, controller_type):
        self.body = Object.Body(x, y, target_type)
        if controller_type == 0:
            self.controller = Controller.Competitive_Controller(self.body)
        elif controller_type == 1:
            self.controller = Controller.Collaborative_Controller(self.body)
        elif controller_type == 2:
            self.controller = Controller.Compassionate_Controller(self.body)
        self.body.controller = self.controller
        self.channels = []
        self.new_messages = []
        self.collected_count = 0
        self.heading = []
        self.visited = []
        self.next_move = []

    def sendMessage(self, channel, message):
        channel.sendMessage(self, message)

    def readNewMessage(self):
        for i in self.new_messages:
        # read message
        self.new_messages.
        del (i)
