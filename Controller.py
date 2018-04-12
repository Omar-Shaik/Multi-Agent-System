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
        self.last_pos = []
        self.steps = 0
        self.stop = False
        self.channels = {}
        self.new_messages = []
        self.other_targets = []

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
                    self.last_pos.append(self.body.position)
                    if len(self.last_pos) == 101:
                        del self.last_pos[0]
                    self.body.move(self.next_mov)
                    self.new_mov = 0
                    moved = True
                    if self.body.position in self.headings:
                        self.headings.remove(self.body.position)
                else:
                    self.getNext()

    def getNext(self):
        if not self.headings:
            got_next = False
            mov = None
            while not got_next:
                x = random.randint(-1, 1)
                y = random.randint(-1, 1)
                mov = [x, y]
                pos = [self.body.position[0] + mov[0], self.body.position[1] + mov[1]]
                got_next = self.environment.validPosition(pos, True)
                if got_next and pos in self.last_pos:
                    got_next = False
            self.steer(mov)
        else:
            got_next = False
            can_go_up = self.environment.validPosition([self.body.position[0] + self.up[0], self.body.position[1] + self.up[1]], True)
            can_go_right = self.environment.validPosition([self.body.position[0] + self.right[0], self.body.position[1] + self.right[1]], True)
            can_go_down = self.environment.validPosition([self.body.position[0] + self.down[0], self.body.position[1] + self.down[1]], True)
            can_go_left = self.environment.validPosition([self.body.position[0] + self.left[0], self.body.position[1] + self.left[1]], True)

            if self.headings[0][0] - self.body.position[0] != 0:
                if self.headings[0][0] - self.body.position[0] > 0 and can_go_right:
                    self.steer(self.right)
                    got_next = True
                elif self.headings[0][0] - self.body.position[0] < 0 and can_go_left:
                    self.steer(self.left)
                    got_next = True
            if not got_next:
                if self.headings[0][1] - self.body.position[1] > 0 and can_go_up:
                    self.steer(self.up)
                elif self.headings[0][1] - self.body.position[1] < 0 and can_go_down:
                    self.steer(self.down)
                else:
                    self.steer(self.stay)


class Competitive_Controller(Controller):
    def __init__(self, body, env):
        Controller.__init__(self, body, env)

    def readMessages(self):
        for i in self.new_messages:
            if i[0] == "Head":
                self.headings.append(i[1])
            elif i[0] == "Done":
                self.stop = True

    def scan(self):
        visible = self.environment.objectsAround(self.body, False)
        if self.collected == self.environment.targets_per_agent:
            self.stop = True
            self.environment.public_channel.sendMessage(self, ["Done", self.body.target_type])
        if visible:
            print "Haha, I know where these are."
            for i in visible:
                print i.target_type


class Collaborative_Controller(Controller):
    def __init__(self, body, env):
        Controller.__init__(self, body, env)

    def readMessages(self):
        for i in self.new_messages:
            if i[0] == "Head":
                self.headings.append(i[1])
                self.new_messages.remove(i)

    def scan(self):
        visible = self.environment.objectsAround(self.body, True)
        if self.collected == self.environment.targets_per_agent:
            self.stop = True
            self.environment.public_channel.sendMessage(self, ["Done", self.body.target_type])

        for i in visible:
            if i.position not in self.other_targets:
                self.other_targets.append(i.position)
                message = ["Head", i.position]
                self.channels[i.target_type].sendMessage(self, message)
                print message


class Compassionate_Controller(Controller):
    def __init__(self, body, env):
        Controller.__init__(self, body, env)

    def readMessages(self):
        for i in self.new_messages:
            if i[0] == "Head":
                self.headings.append(i[1])
                self.new_messages.remove(i)
            elif i[0] == "Done":
                self.stop = True

    def scan(self):
        visible = self.environment.objectsAround(self.body, True)
        if self.collected == self.environment.targets_per_agent:
            self.stop = True
            self.environment.public_channel.sendMessage(self, ["Done", self.body.target_type])

        for i in visible:
            if i.position not in self.other_targets:
                self.other_targets.append(i.position)
                message = ["Head", i.position]
                self.channels[i.target_type].sendMessage(self, message)
