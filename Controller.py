import random

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
        self.steps = 0
        self.stop = False
        self.channels = {}

    def steer(self, dir):
        self.next_mov = dir
        self.new_mov = 1

    def goToNext(self):
        if self.stop:
            self.steer(self.stay)
        else:
            moved = False
            while not moved:
                if self.new_mov == 1:
                    self.body.move(self.next_mov)
                    moved = True
                    if self.body.position in self.headings:
                        self.headings.remove(self.body.position)
                else:
                    self.getNext()

    def getNext(self):
        if not self.headings:
            got_next = False
            while not got_next:
                pos = [self.body.position[0] + random.randint(0, 1), self.body.position[1] + random.randint(0, 1)]
                got_next = self.environment.validPosition(pos)
                self.steer(pos)
        else:
            got_next = False
            if self.headings[0][0] - self.body.position[0] != 0:
                if self.headings[0][0] - self.body.position[0] > 0:
                    if self.environment.validPosition([self.body.position[0] + self.right[0], self.body.position[1] + self.right[1]]):
                        self.steer(self.right)
                        got_next = True
                else:
                    if self.environment.validPosition([self.body.position[0] + self.left[0], self.body.position[1] + self.left[1]]):
                        self.steer(self.left)
                        got_next = True
            if not got_next:
                if self.headings[0][1] - self.body.position[1] > 0:
                    if self.environment.validPosition([self.body.position[0] + self.up[0], self.body.position[1] + self.up[1]]):
                        self.steer(self.up)
                    else:
                        self.steer(self.stay)
                else:
                    if self.environment.validPosition([self.body.position[0] + self.down[0], self.body.position[1] + self.down[1]]):
                        self.steer(self.down)
                    else:
                        self.steer(self.stay)


class Competitive_Controller(Controller):
    def __init__(self, body, env):
        Controller.__init__(self, body, env)

    def readMessages(self):
        for i in self.body.new_messages:
            if i[0] == "head":
                self.headings.append(i[1])
            else:
                self.stop = True

    def scan(self):
        visible = self.environment.objectsAround(self)


class Collaborative_Controller(Controller):
    def __init__(self, body, env):
        Controller.__init__(self, body, env)

    def readMessages(self):
        for i in self.body.new_messages:
            if i[0] == "head":
                self.headings.append(i[1])

    def scan(self):
        visible = self.environment.objectsAround(self)
        if self.collected < self.environment.number_of_targets:
            self.stop = True

        for i in self.environment.visible:
            self.channels[i.object_type].sendMessage(self, ["Head", i.position])


class Compassionate_Controller(Controller):
    def __init__(self, body, env):
        Controller.__init__(self, body, env)

    def readMessages(self):
        for i in self.body.new_messages:
            if i[0] == "head":
                self.headings.append(i[1])
        else:
            self.stop = True

    def scan(self):
        visible = self.environment.objectsAround(self)
        if self.collected < self.environment.number_of_targets:
            self.stop = True

        for i in visible:
            self.channels[i.object_type].sendMessage(self, ["Head", i.position])
