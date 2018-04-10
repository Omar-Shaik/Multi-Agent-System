import math
import random
import string
import Communication
import Agent
import Object

class Environment:
    # Create new environment with the given bounds
    # Populates an environment with the number of agents and number of targets per agent specified.
    # Found space variable makes sure it's safe to add the randomly generated agent. Only becomes true when position is valid.

    def __init__(self, x_lower, y_lower, length, height, number_of_agents, targets_per_agent, controller_type):
        self.x_lower = x_lower
        self.y_lower = y_lower
        self.x_upper = x_lower + length
        self.y_upper = y_lower + height
        self.target_types = list(string.ascii_uppercase)
        self.agents = []
        self.targets = []
        self.public_channel = Communication.CommunicationChannel(0)
        for i in range(number_of_agents):
            found_space = False
        
            while not found_space:
                position = [random.randint(self.x_lower, self.x_upper), random.randint(self.y_lower, self.y_upper)]
                found_space = self.validPosition(position)
            agent = Agent.Agent(self, position[0], position[1], self.target_types[i], controller_type, targets_per_agents)
            self.public_channel.addAccess(agent)
            agent.controller.channels.append(self.public_channel)
            self.agents.append(agent)
        
            for j in range(targets_per_agent):
                found_space = False
                while not found_space:
                    position = [random.randint(self.x_lower, self.x_upper), random.randint(self.y_lower, self.y_upper)]
                    found_space = self.validPosition(position)
                target = Object.Target(position[0], position[1], self.target_types[i])
                self.targets.append(target)
        i = 0
        while i < len(agents) - 2:
            j = i + 1
            while j < len(agents) - 1:
                channel = Communication.CommunicationChannel(1)
                agent1 = agents[i]
                agent2 = agents[j]
                channel.addAccess(agent1)
                agent1.controller.channels[agent2.body.object_type] = channel
                channel.addAccess(agent2)
                agent2.controller.channels[agent1.body.object_type] = channel
                j += 1
            i += 1


# Function checks if proposed position is valid.
# Validity variable holds the validity of the position. Only changes if position is invalid.
# Avoids unnecessary entry if first condition makes the position invalid.
# First if statement checks if the position is in the bounds of the environment.
# Second if statement is a loop that compares the position of every object currently in the environment with the proposed position.
# Third if statement within second checks if that position is currently occupied.
# Third if statement also makes sure that two agents don't get too close to one another. Their radars cannot overlap, meaning 20cm.

    def validPosition(self, position):
        validity = True

        if position[0] >= self.x_upper or position[0] <= self.x_lower or position[1] >= self.y_upper or position[1] <= self.y_lower:
            validity = False

        if validity:
            for t in self.targets:
                if t.pos[0] == position[0] and t.pos[1] == position[1]:
                    validity = False

        return validity
    
     def colisionAvoidance(self, controller):
        for a in self.agents:
            if self.distance(a, controller.body) < 20:
                return False
            else:
                return True



# Returns a list of elements visible to the body.
# Removes targets that have the same target type as the body from the environment if they are within radar range.

    def objectsAround(self, body, need_visible):
        visible = []

        for t in self.targets:
            if self.distance(body, t) <= 10:
                if body.target_type == t.target_type:
                    self.targets.remove(t)
                    body.Controller.collected += 1

                else:
                    visible.append(t)

        if need_visible:
            return visible

#Returns euclidean distance between two objects: o1 and o2
    def distance(self, o1, o2):
        return math.sqrt((o1.pos[0] - o2.pos[0]) ** 2 + (o1.pos[1] - o2.pos[1]) ** 2)
    
